# PDF_Interweaver
Interweaves two PDF documents for easy visual comparison of pages.

## About this tool

The human brain is incredibly adept at identifying visual changes between two images. A study by Luzzo and Drury from 1980 tested the concept of "blinking" as a proven method for improving the identification of circuit board defects by "blinking" images of the production circuit board back and forth with an image of a "good" circuit board, thereby allowing the deviations to effectively become emergent features.

This tool leverages this concept to be applied in the comparison of two nearly-identical PDF documents. Specifically, this tool will combine two PDF documents by "interweaving" the pages of separate PDFs into a merged PDF, with one page of each document being merged together (e.g. for PDF A and PDF B, the output PDF would consist of pages A1, B1, A2, B2, A3, B3…). This allows the user to review the output PDF and rapidly look for visual differences by opening the PDF document and quickly flipping back and forth between successive pages, effectively "blinking" two images to identify discrepancies.

## Practical Applications

The applications of this tool found most personally useful have been in the review of contracts; specifically, being able to quickly identify changes between two documents and verify consistency in other aspects. Examples of this include ensuring all parts of a contract remain the same, save for a minor modification; verifying no content has changed and no additional provisions inserted between two versions of a document; comparing documents in various versions; etc. This tool has already allowed me to catch errors in vendor quotes, regressions between redlined legal documents and erroneously "final" PDFs, surreptitiously-inserted terms into contracts, and other similar contractual modifications.

## Usage

With the PyPDF2 package installed, execute `python3 -m pdf_interweaver.pdf` with the following parameters:

- **Filepath 1** (Required): Filepath of the first PDF file to merge. Typically reflects the "original," "base," or "good" PDF.
- **Filepath 2** (Required): Filepath of the second PDF file to merge. Typically reflects the "new," "updated," or "comparison" PDF.
- **`--w` Watermark** (Optional): Filepath of a PDF to overlay on _both_ files.
- **`--wm1` Watermark 1** (Optional): Filepath of a PDF to overlay on pages from the first PDF file.
- **`--wm2` Watermark 2** (Optional): Filepath of a PDF to overlay on pages from the second PDF file.

To add a watermark of a "Base" or "New" label, generate a PDF with translucent text in a document processor and use the exported PDF's filepath as the overlay PDF above.

For help, run with parameter `-h`.
