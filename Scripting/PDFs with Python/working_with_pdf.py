import PyPDF2

with open("tesla.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open("new_document.pdf", "wb") as new_file:
        writer.write(new_file)
