""""------------------------------------------------------------------
PDF Interweaver
(c) Jeff Kessler, 2024-08-25-1805

2023-08-13-0855-JK  Fix for unequal page numbers
                    Distinct filenames
2024-08-25-1805-JK  Updates for PyPDF2 v3
------------------------------------------------------------------"""

import PyPDF2
import time

#input("Filepath 1: ")

def pdf_merger(original_fp, new_fp, watermark, mark1, mark2):

    # Open PDF Files
    a = PyPDF2.PdfReader(original_fp)
    b = PyPDF2.PdfReader(new_fp)


    # Open Watermark files
    if watermark:
        watermark_pdf = PyPDF2.PdfReader(watermark)
        watermark = watermark_pdf.pages[0]

    if mark1:
        mark1_pdf = PyPDF2.PdfReader(mark1)
        mark1 = mark1_pdf.pages[0]

    if mark2:
        mark2_pdf = PyPDF2.PdfReader(mark2)
        mark2 = mark2_pdf.pages[0]


    # Determine common page count
    common_page_count = min(len(a.pages), len(b.pages))


    # Establish merged PDF
    merged = PyPDF2.PdfWriter()


    # Iteratively add common pages
    for pagenum in range(common_page_count):
        pagea = a.pages[pagenum]
        pageb = b.pages[pagenum]
        if mark1:
            pagea.merge_page(mark1)
        if mark2:
            pageb.merge_page(mark2)
        if watermark:
            pagea.merge_page(watermark)
            pageb.merge_page(watermark)
        merged.add_page(pagea)
        merged.add_page(pageb)

    # Add Unique Pages
    for pagenum in range(common_page_count, len(a.pages)):
        pagea = a.pages[pagenum]
        if mark1:
            pagea.merge_page(mark1)
        if watermark:
            pagea.merge_page(watermark)
            pageb.merge_page(watermark)
        merged.add_page(pagea)
        merged.add_blank_page()

    for pagenum in range(common_page_count, len(b.pages)):
        pageb = b.pages[pagenum]
        if mark2:
            pageb.merge_page(mark2)
        if watermark:
            pagea.merge_page(watermark)
            pageb.merge_page(watermark)
        merged.add_blank_page()
        merged.add_page(pageb)


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
