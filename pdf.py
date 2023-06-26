"""Module providingFunction printing python version."""
import sys
import PyPDF2

inputs = sys.argv[1:]

"""Module has a function that prints the name of my site"""
def pdf_combiner(pdf_list):
    """Function printing the name of my site"""
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combiner(inputs)
