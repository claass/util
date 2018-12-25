import pandas as pd
import argparse


def parse_args():
    """Get CLI arguments passed by user"""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input_file",
        required=True,
        help="path to csv input file",
        type=str
    )
    parser.add_argument(
        "-o",
        "--output_folder",
        required=True,
        help="path to output folder",
        type=str
    )
    parser.add_argument(
        "-f",
        "--output_file",
        required=True,
        help="prefix for output filed (no extension)",
        type=str
    )
    parser.add_argument(
        "-b",
        "--split_by",
        required=True,
        help="column name to split by",
        type=str
    )
    args = parser.parse_args()
    return args


def split_csv(input_file, output_folder, output_file, split_by):
    """
    Splits csv file by values in a specfied column and
    stores them in the output folder.

    Args:
        input_file (str):   path to csv to be split
        output_folder (str):  folder to save chunks to
        output_file (str):  prefix for output chunks
        split_by (str):     column name to split the input csv by
    """
    
    df = pd.read_csv(input_file)
    for val in df[split_by].unique():
        sub_df = df[df[split_by] == val]
        filename = output_folder + output_file + '__' + val + ".csv"
        sub_df.to_csv(filename, index=False)


if __name__ == '__main__':
    arguments = parse_args()
    split_csv(
        arguments.input_file,
        arguments.output_path,
        arguments.output_file,
        arguments.split_by
    )
    print("==== Complete ====")
