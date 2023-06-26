from pypdf import PdfReader

reader = PdfReader("888497.pdf")
print(len(reader.pages))
for page in reader.pages:
    print(page.extract_text())