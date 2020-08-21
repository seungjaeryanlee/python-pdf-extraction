"""
Run pdfplumber on sample PDFs.

Install with `pip install pdfplumber`.
"""
import pdfplumber


with open("pdfplumber.out", "w") as f:
    with pdfplumber.open("pdfs/1412.6980.pdf") as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            f.write(text)
