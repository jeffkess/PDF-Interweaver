""""------------------------------------------------------------------
PDF Interweaver
(c) Jeff Kessler, 2019-06-15-1710

2023-08-13-0855-JK  Fix for unequal page numbers
                    Distinct filenames
------------------------------------------------------------------"""

import PyPDF2
import time

#input("Filepath 1: ")

def pdf_merger(original_fp, new_fp, watermark, mark1, mark2):

    # Open PDF Files
    a = PyPDF2.PdfFileReader(original_fp)
    b = PyPDF2.PdfFileReader(new_fp)


    # Open Watermark files
    if watermark:
        watermark_pdf = PyPDF2.PdfFileReader(watermark)
        watermark = watermark_pdf.getPage(0)

    if mark1:
        mark1_pdf = PyPDF2.PdfFileReader(mark1)
        mark1 = mark1_pdf.getPage(0)

    if mark2:
        mark2_pdf = PyPDF2.PdfFileReader(mark2)
        mark2 = mark2_pdf.getPage(0)


    # Determine common page count
    common_page_count = min(a.numPages, b.numPages)


    # Establish merged PDF
    merged = PyPDF2.PdfFileWriter()


    # Iteratively add common pages
    for pagenum in range(common_page_count):
        pagea = a.getPage(pagenum)
        pageb = b.getPage(pagenum)
        if mark1:
            pagea.mergePage(mark1)
        if mark2:
            pageb.mergePage(mark2)
        if watermark:
            pagea.mergePage(watermark)
            pageb.mergePage(watermark)
        merged.addPage(pagea)
        merged.addPage(pageb)

    # Add Unique Pages
    for pagenum in range(common_page_count, a.numPages):
        pagea = a.getPage(pagenum)
        if mark1:
            pagea.mergePage(mark1)
        if watermark:
            pagea.mergePage(watermark)
            pageb.mergePage(watermark)
        merged.addPage(pagea)
        merged.addBlankPage()

    for pagenum in range(common_page_count, b.numPages):
        pageb = b.getPage(pagenum)
        if mark2:
            pageb.mergePage(mark2)
        if watermark:
            pagea.mergePage(watermark)
            pageb.mergePage(watermark)
        merged.addBlankPage()
        merged.addPage(pageb)


    # Save Merged PDF
    with open(f'Merged PDF Generated {time.strftime("%Y-%m-%d-%H%M%S")}.pdf', "wb") as file:
        merged.write(file)


if __name__=="__main__":

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('fp1', type=str, help='Original filepath')
    parser.add_argument('fp2', type=str, help='New filepath')
    parser.add_argument('--wm', "--w", help="Filepath of PDF watermark to apply to both pages")
    parser.add_argument('--m1', "--wm1", "--mark1", help="Filepath of PDF watermark to apply to the original PDF")
    parser.add_argument('--m2', "--wm2", "--mark2", help="Filepath of PDF watermark to apply to the new PDF")
    args = parser.parse_args()
    pdf_merger(args.fp1, args.fp2, args.wm, args.m1, args.m2)
