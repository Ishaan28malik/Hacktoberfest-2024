#INSTALL -> PyPDF2
#FORMAT ->  python3 merging_pdfs.py filename1 filename2

import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write('merged.pdf')

pdf_combiner(inputs)
