import argparse
import os

import torch
from tqdm import tqdm
from dl4phylo.data import load_tree, load_data, DataType

def make_tensors(tree_dir: str, data_dir: str, out_dir: str, data_type: DataType):
    tensors_dir = os.path.join(out_dir, data_dir.split("\\")[-1])
    if not os.path.exists(tensors_dir):
        os.mkdir(tensors_dir)


    trees = [file for file in os.listdir(tree_dir) if file.endswith(".nwk")]
    for tree_file in (pbar := tqdm(trees)):
        identifier = tree_file.rstrip(".nwk")
        pbar.set_description(f"Processing {identifier}")
        tree_tensor, _ = load_tree(os.path.join(tree_dir, tree_file))
        file_extension = ".txt" if data_type == DataType.TYPING else ".fasta"
        data_tensor, _ = load_data(os.path.join(data_dir, f"{identifier}{file_extension}"), data_type)

        torch.save(
            {"X": data_tensor, "y": tree_tensor},
            os.path.join(tensors_dir, f"{identifier}.tensor_pair"),
        )

DATA_TYPES = DataType.toList()

def main():
    parser = argparse.ArgumentParser(
        description="Generate a tensor training set from trees and MSAs"
    )
    parser.add_argument(
        "-t",
        "--treedir",
        required=True,
        type=str,
        help="path to input directory containing the .nwk tree files",
    )
    parser.add_argument(
        "-dd",
        "--datadir",
        required=True,
        type=str,
        help="path to input directory containing corresponding\
            data files: [.fasta for alignments or .txt for typing data]",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=False,
        default=".",
        type=str,
        help="path to output directory",
    )
    parser.add_argument(
        "-dt",
        "--data_type",
        required=False,
        default=DataType.AMINO_ACIDS.name,
        choices=DATA_TYPES,
        type=str,
        help=f"type of input data. Allowed values: {DATA_TYPES}",
    )
    args = parser.parse_args()

    make_tensors(args.treedir, args.datadir, args.output, DataType[args.data_type])


if __name__ == "__main__":
    main()
