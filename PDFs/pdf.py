import PyPDF2

with open(r"C:\Users\14058\OneDrive\Desktop\Programming\Python Stuff\PDFs\PdfPages\dummy.pdf", "rb") as new_file:
    # converting file object to binary so it can be read
    reader = PyPDF2.PdfFileReader(new_file)
    print(reader.numPages)
    # print(reader.getPage(0)) # to get first page
    first_page = reader.getPage(0)
    # print(first_page.rotateClockwise(180)) # rotate page(need to get page first to do so)

    first_page.rotateClockwise(180)
    file_writer = PyPDF2.PdfFileWriter(); # creating filewriter object
    file_writer.addPage(first_page) # adding rotated page to this object

    # to write contents of previous pdf to another one
    with open(r"C:\Users\14058\OneDrive\Desktop\Programming\Python Stuff\PDFs\PdfPages\new_dummy.pdf", "wb") as output_file:
        file_writer.write(output_file)
