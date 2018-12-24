import pandas as pd


def split_csv(input_file, output_path, output_file, split_by):
    """
    Splits csv file by values in a specfied column and
    stores them in the output folder.

    Args:
        input_file (str):   path to csv to be split
        output_path (str):  folder to save chunks to
        output_file (str):  prefix for output chunks
        split_by (str): column name to split the input csv by
    """
    df = pd.read_csv(input_file)
    for val in df[split_by].unique():
        sub_df = df[df[split_by] == val]
        filename = output_path + output_file + '__' + val + ".csv"
        sub_df.to_csv(filename, index=False)


if __name__ == '__main__':
    input_file = input('Path to input csv: ')
    output_path = input('Path to store output: ')
    output_file = input('Prefix for output chunks: ')
    split_by = input('Column name to split csv by: ')
    split_csv(input_file, output_path, output_file, split_by)
    print("==== Complete ====")
