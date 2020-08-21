"""
Run PyMuPDF parser on sample PDFs.

Install with `pip install pymupdf`.
"""
import fitz


def get_text(filepath: str) -> str:
    with fitz.open(filepath) as doc:
        text = ""
        for page in doc:
            text += page.getText().strip()
        return text

with open("pymupdf.out", "w") as f:
    text = get_text("pdfs/1412.6980.pdf")
    f.write(text)
