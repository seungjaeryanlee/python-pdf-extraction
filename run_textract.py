"""
Run textract parser on sample PDFs.

Install with `pip install textract`.
"""
import textract


text = textract.process("pdfs/1412.6980.pdf")

with open("textract.out", "wb") as f:
    f.write(text)
