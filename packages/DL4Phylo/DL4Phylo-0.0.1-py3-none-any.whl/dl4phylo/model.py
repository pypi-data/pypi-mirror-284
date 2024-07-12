"""The DL4Phylo module contains the DL4Phylo network as well as functions to 
create and load instances of the network from disk
"""
from typing import Any, Dict, List, Tuple, Optional

import skbio
import torch
import torch.nn as nn
from ete3 import Tree
from scipy.special import binom

from dl4phylo.attentions import KernelAxialMultiAttention


class AttentionNet(nn.Module):
    """DL4Phylo Network"""

    def __init__(
        self,
        n_blocks: int = 1,
        n_heads: int = 4,
        h_dim: int = 64,
        dropout: float = 0.0,
        device: str = "cpu",
        n_data: int = 20,
        data_len: int = 200,
        in_channels: int = 22,
        **kwargs
    ):
        """Initializes internal Module state

        Parameters
        ----------
        n_blocks : int, optional
            Number of blocks in transformer, by default 1
        n_heads : int, optional
            Number of heads in multi-head attention, by default 4
        h_dim : int, optional
            Hidden dimension, by default 64
        dropout : float, optional
            Droupout rate, by default 0.0
        device : str, optional
            Device for model ("cuda" or "cpu"), by default "cpu"
        n_data : int, optional
            Number of sequences in input alignments, by default 20
        data_len : int, optional
            Length of sequences in input alignment, by default 200
        in_channels : int, optional
            Number of channels in input tensor, depending on input type [nucleotides: 4, aminoacids: 22, typing data: 32]
        

        Returns
        -------
        AttentionNet
            Functional instance of AttentionNet for inference/fine-tuning

        Raises
        ------
        ValueError
            If h_dim is not divisible by n_heads
        """

        if h_dim % n_heads != 0:
            raise ValueError(
                "The embedding dimension (h_dim) must be divisible"
                "by the number of heads (n_heads)!"
            )

        super(AttentionNet, self).__init__()
        # Initialize variables
        self.n_blocks = n_blocks
        self.n_heads = n_heads
        self.h_dim = h_dim
        self.dropout = dropout
        self.device = device
        self.in_channels = in_channels

        self._init_seq2pair(n_data, data_len)

        # Initialize Module lists
        self.rowAttentions = nn.ModuleList()
        self.columnAttentions = nn.ModuleList()
        self.layernorms = nn.ModuleList()
        self.fNNs = nn.ModuleList()

        # Position wise fully connected layer from pair wise averaging procedure
        layers_1_1 = [
            nn.Conv2d(in_channels=in_channels, out_channels=h_dim, kernel_size=1, stride=1),
            nn.ReLU(),
        ]
        self.block_1_1 = nn.Sequential(*layers_1_1)
        
        # Normalization layer
        self.norm = nn.LayerNorm(h_dim)

        # Position wise fully connected layer from site wise averaging procedure
        self.pwFNN = nn.Sequential(
            *[
                nn.Conv2d(in_channels=h_dim, out_channels=1, kernel_size=1, stride=1),
                nn.Dropout(dropout),
                nn.Softplus(),
            ]
        )

        for i in range(self.n_blocks):
            self.rowAttentions.append(
                KernelAxialMultiAttention(h_dim, n_heads, n=data_len).to(device)
            )
            self.columnAttentions.append(
                KernelAxialMultiAttention(h_dim, n_heads, n=int(binom(n_data, 2))).to(device)
            )
            self.layernorms.append(nn.LayerNorm(h_dim).to(device))
            self.fNNs.append(
                nn.Sequential(
                    *[
                        nn.Conv2d(
                            in_channels=h_dim,
                            out_channels=h_dim * 4,
                            kernel_size=1,
                            stride=1,
                            device=device,
                        ),
                        nn.Dropout(dropout),
                        nn.GELU(),
                        nn.Conv2d(
                            in_channels=h_dim * 4,
                            out_channels=h_dim,
                            kernel_size=1,
                            stride=1,
                            device=device,
                        ),
                    ],
                    nn.Dropout(dropout)
                )
            )

    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, List[Any]]:
        """Does a forward pass through the DL4Phylo network

        Parameters
        ----------
        x : torch.Tensor
            Input tensor (shape 1\*encoding_size\*n_data\*data_len)

        Returns
        -------
        torch.Tensor
            Output tensor (shape 1\*n_pairs)
        List[Any]
            Attention maps

        Raises
        ------
        ValueError
            If the tensors aren't the right shape
        """
        # Check if the input tensor has the right shape
        if x.shape[1:] != (self.in_channels, self.data_len, self.n_data):
            raise ValueError(
                f"Input tensor shape is: {x.shape[1:]}; but ({self.in_channels}, {self.data_len}, {self.n_data}) was expected."
            )

        # 2D convolution that gives us the features in the third dimension
        # (i.e. initial embedding of each amino acid)
        out = self.block_1_1(x) # [4, 64, 200, 20]

        # Pair representation
        out = torch.matmul(self.seq2pair, out.transpose(-1, -2)) # [4, 64, 190, 200]

        # From here on the tensor has shape = (batch_size,features,nb_pairs,data_len), all
        # the transpose/permute allow to apply layernorm and attention over the desired
        # dimensions and are then followed by the inverse transposition/permutation
        # of dimensions

        out = self.norm(out.transpose(-1, -3)).transpose(-1, -3) # layernorm

        for i in range(self.n_blocks):
            # AXIAL ATTENTIONS BLOCK
            # ----------------------
            # ROW ATTENTION

            # out.permute(0, 2, 3, 1) = [4, 190, 200, 64]
            att = self.rowAttentions[i](out.permute(0, 2, 3, 1))

            # att.permute(0, 3, 1, 2) = [4, 64, 190, 200]
            out = att.permute(0, 3, 1, 2) + out  # row attention + residual connection

            # layernorm
            out = self.layernorms[i](out.transpose(-1, -3)).transpose(-1, -3)

            # ----------------------
            # COLUMN ATTENTION

            # out.permute(0, 3, 1, 2) = [4, 190, 200, 64]
            att = self.columnAttentions[i](out.permute(0, 3, 2, 1))

            # att.permute(0, 3, 1, 2) = [4, 64, 190, 200]
            out = att.permute(0, 3, 2, 1) + out  # column attention + residual connection

            # layernorm
            out = self.layernorms[i](out.transpose(-1, -3)).transpose(-1, -3)

            # ----------------------
            # FEEDFORWARD
            out = self.fNNs[i](out) + out

            # Applies the normalization between transformer blocks
            if i != self.n_blocks - 1:
                out = self.layernorms[i](out.transpose(-1, -3)).transpose(-1, -3)  # layernorm

        # shape = (batch_size, 1, nb_pairs, data_len) --> [4, 1, 190, 200]
        out = self.pwFNN(out)

        # Averaging over positions and removing the extra dimensions
        # we finally get shape = (batch_size, nb_pairs) --> [4, 190]
        out = torch.squeeze(torch.mean(out, dim=-1))

        return out

    def _init_seq2pair(self, n_data: int, data_len: int):
        """Initialize Seq2Pair matrix"""

        self.n_data = n_data
        self.data_len = data_len

        # Calculate all possible combinations of 2 sequences
        self.n_pairs = int(binom(n_data, 2))

        # Create a tensor with zeros of dimensions (n_pairs, n_data)
        seq2pair = torch.zeros(self.n_pairs, self.n_data)

        """
            Iterates over the created tensor and places the value 1
            in the positions that indicate which sequences belong to each pair.

            For example: The pair 1 will be constituted by sequence 1 and 2, thus
            the positions [0,0] and [0,1] of the tensor will have the value 1.

            In our example the tensor will look like this:
                      seqs
                    [1, 1, 0]
              pairs [1, 0, 1]
                    [0, 1, 1]
        """
        k = 0
        for i in range(self.n_data):
            for j in range(i + 1, self.n_data):
                seq2pair[k, i] = 1
                seq2pair[k, j] = 1
                k = k + 1

        self.seq2pair = seq2pair.to(self.device)

    def _get_architecture(self) -> Dict[str, Any]:
        """Returns architecture parameters of the model

        Returns
        -------
        Dict[str, Any]
            Dictionnary containing model architecture
        """
        return {
            "n_blocks": self.n_blocks,
            "n_heads": self.n_heads,
            "h_dim": self.h_dim,
            "dropout": self.dropout,
            "data_len": self.data_len,
            "n_data": self.n_data,
            "in_channels": self.in_channels,
        }

    def save(self, path: str) -> None:
        """Saves the model parameters to disk

        Parameters
        ----------
        path : str
            Path to save the model to
        """
        torch.save(
            {
                "architecture": self._get_architecture(),
                "state_dict": self.state_dict(),
            },
            path,
        )
    
    def infer_dm(
        self, X: torch.Tensor, ids: Optional[list[str]] = None
    ) -> skbio.DistanceMatrix:
        """Infers a phylogenetic distance matrix from embedded alignment tensor

        Parameters
        ----------
        X : torch.Tensor
            Input alignment, embedded as a tensor (shape encoding_size\*n_seq\*data_len)
        ids : list[str], optional
            Identifiers of the sequences in the input tensor, by default None

        Returns
        -------
        skbio.DistanceMatrix
            Phylolgenetic distance matrix inferred by DL4Phylo

        Raises
        ------
        ValueError
            If the tensors aren't the right shape
        """
                # Check if the input tensor has the right shape
        if X.shape != (self.in_channels, self.data_len, self.n_data):
            raise ValueError(
                f"Input tensor shape is: {X.shape}; but ({self.in_channels}, {self.data_len}, {self.n_data}) was expected."
            )

        # reshape from [22, n_seq, data_len] to [1, 22, n_seq, data_len]
        tensor = X[None, :, :]
        tensor = tensor.to(self.device)

        # Infer distances
        with torch.no_grad():
            predictions = self(tensor.float())
        predictions = predictions.view(self.n_pairs)

        # Build distance matrix
        nn_dist = {}
        cursor = 0
        for i in range(self.n_data):
            for j in range(self.n_data):
                if i == j:
                    nn_dist[(i, j)] = 0
                if i < j:
                    pred = predictions[cursor].item()
                    pred = float("%.6f" % (pred))
                    nn_dist[(i, j)], nn_dist[(j, i)] = pred, pred
                    cursor += 1

        return skbio.DistanceMatrix(
            [[nn_dist[(i, j)] for j in range(self.n_data)] for i in range(self.n_data)],
            ids=ids,
        )

    def infer_tree(
        self,
        X: torch.Tensor,
        ids: Optional[list[str]] = None,
        dm: Optional[skbio.DistanceMatrix] = None,
    ) -> Tree:
        """Infers a phylogenetic tree from an embedded alignment tensor

        Parameters
        ----------
        X : torch.Tensor
            Input alignment, embedded as a tensor (shape encoding_size\*n_seq\*data_len)
        ids : list[str], optional
            Identifiers of the sequences in the input tensor, by default None
        dm : skbio.DistanceMatrix, optional
            Precomputed distance matrix if you have already run `AttentionNet.infer_dm`
            on your own, by default None

        Returns
        -------
        Tree
            Phylogenetic tree computed with neighbour joining from the distance matrix
            inferred by DL4Phylo

        Raises
        ------
        ValueError
            If the tensors aren't the right shape
        """
        # Check if the input tensor has the right shape
        if X.shape != (self.in_channels, self.data_len, self.n_data):
            raise ValueError(
                f"Input tensor shape is: {X.shape}; but ({self.in_channels}, {self.data_len}, {self.n_data}) was expected."
            )

        dl4phylo_dm = dm if dm is not None else self.infer_dm(X, ids)
        nn_newick_str = skbio.tree.nj(dl4phylo_dm, result_constructor=str)

        return Tree(nn_newick_str)

def _init_model(model: AttentionNet, state_dict: dict, single_gpu: bool):
    """Loads a state_dict into a DL4Phylo model

    Parameters
    ----------
    model : AttentionNet
        Phyloformer model to populate
    state_dict : dict
        State dict to populate the model with
    single_gpu: bool
        Wether inference/fine-tuning will be done on a single GPU
    """

    # Remove "module." from keys for models trained on multiple gpus
    new_state_dict = (
        {k.replace("module.", ""): v for k, v in state_dict.items()}
        if single_gpu
        else state_dict
    )

    model.load_state_dict(new_state_dict, strict=True)


def load_model(path: str, device: str = "cpu", single_gpu: bool = True) -> AttentionNet:
    """Load a DL4Phylo istance froms disk

    Parameters
    ----------
    path : str
        Path to model saved with AttentionNet.save()
    device : str, optional
        Device to load model to ("cpu" or "cuda"), by default "cpu"
    single_gpu: bool, optional
        Wether inference/fine-tuning will be done on a single GPU, by default True

    Returns
    -------
    AttentionNet
        Functional instance of AttentionNet for inference/fine-tuning

    Raises
    ------
    ValueError
        If the file does not contain the state_dict and model architecture parameters
    """

    loaded = torch.load(path, map_location=device)
    if loaded.get("state_dict") is None or loaded.get("architecture") is None:
        raise ValueError(
            "Error loading model. Saved file must contain both a 'state_dict' "
            "and a 'architecture' entry"
        )

    # loaded["architecture"].pop("device")
    model = AttentionNet(**loaded["architecture"], device=device)
    _init_model(model, loaded["state_dict"], single_gpu)
    model.to(device)

    return model
