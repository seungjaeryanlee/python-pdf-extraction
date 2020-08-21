"""
Run tika parser on sample PDFs.

Install with `pip install tika`. Requires Java 7+ installed on your system.
"""
from tika import parser


rawText = parser.from_file("pdfs/1412.6980.pdf")
rawList = rawText["content"].splitlines()
with open("tika.out", "w") as f:
    for line in rawList:
        f.write(line + "\n")
