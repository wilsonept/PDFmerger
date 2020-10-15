import PyPDF2
import os

def merge(basedir):
	os.chdir(basedir)
	files = os.listdir()

	writer = PyPDF2.PdfFileWriter()

	pdfFiles = []

	for file in files:
		pdfFile = open(file, 'rb')
		pdfFiles.append(pdfFile)

	for pdfFile in pdfFiles:
		file = PyPDF2.PdfFileReader(pdfFile)		
		for pageNum in range(file.numPages):
			page = file.getPage(pageNum)
			writer.addPage(page)

	outputFile = open('combined.pdf', 'wb')
	writer.write(outputFile)
	outputFile.close()

	for pdfFile in pdfFiles:
	    pdfFile.close()

# merge('c:\\!git\\PDFmerger\\process')