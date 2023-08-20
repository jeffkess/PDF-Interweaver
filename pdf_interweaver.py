""""------------------------------------------------------------------
PDF Interweaver
(c) Jeff Kessler, 2019-06-15-1710
------------------------------------------------------------------"""

import PyPDF2

a = PyPDF2.PdfFileReader(input("Filepath 1: "))
b = PyPDF2.PdfFileReader(input("Filepath 2: "))

merged = PyPDF2.PdfFileWriter()

for pagenum in range(min(a.numPages, b.numPages)):
    pagea = a.getPage(pagenum)
    pageb = b.getPage(pagenum)
    merged.addPage(pagea)
    merged.addPage(pageb)

for pagenum in range(a.numPages - min(a.numPages, b.numPages)):
    pagea = a.getPage(pagenum)
    merged.addPage(pagea)

for pagenum in range(b.numPages - min(a.numPages, b.numPages)):
    pageb = b.getPage(pagenum)
    merged.addPage(pageb)

with open("merged.pdf", "wb") as file:
    merged.write(file)