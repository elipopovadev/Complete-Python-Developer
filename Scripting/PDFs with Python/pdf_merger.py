import PyPDF2


inputs = "tesla.pdf", "new_document.pdf"


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)

    merger.write("super.pdf")


pdf_combiner(inputs)
