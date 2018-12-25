import argparse
import contextlib
import PyPDF2
import glob


def parse_args():
    """Get CLI arguments passed by user"""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input_folder",
        required=True,
        help="path to input folder",
        type=str
    )
    parser.add_argument(
        "-o",
        "--output_file",
        required=True,
        help="path and name for output (incl. extension)",
        type=str
    )
    args = parser.parse_args()
    return args


def merge_pdfs(input_folder, output_file):
    """
    Merges PDF files in specified folder in alphabetical order.
    Hotfixes a bug in current version of PyPDF2 that resulted in blank pages.

    Args:
        input_folder (str): paths to pdfs that need to be merged
        output_file  (str): path to output file (including extension)
    """

    # Getting paths for pdf files only
    pdfs = glob.glob(input_folder+"*.pdf")
    pdfs.sort()

    # Merge PDFs by appending and save to output path
    with contextlib.ExitStack() as stack:
        pdfMerger = PyPDF2.PdfFileMerger()
        files = [stack.enter_context(open(pdf, 'rb')) for pdf in pdfs]
        for f in files:
            pdfMerger.append(f)
        with open(output_file, 'wb') as f:
            pdfMerger.write(f)


if __name__ == '__main__':
    arguments = parse_args()
    merge_pdfs(arguments.input_folder, arguments.output_file)
    print('Merge complete.')
