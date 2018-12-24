import contextlib
import PyPDF2


def merge_pdfs(pdfs, output_file):
    """
    Merges PDF files. Hotfixing bug in current version of PyPDF2

    Args:
        pdfs (list, str):   paths to pdfs that need to be merged
        output (str):       path to output file
    """

    with contextlib.ExitStack() as stack:
        pdfMerger = PyPDF2.PdfFileMerger()
        files = [stack.enter_context(open(pdf, 'rb')) for pdf in pdfs]
        for f in files:
            pdfMerger.append(f)
        with open(output_file, 'wb') as f:
            pdfMerger.write(f)
