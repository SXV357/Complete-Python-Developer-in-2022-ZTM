import PyPDF2
import sys
import os

file_inputs = sys.argv[1:]
for file in file_inputs:
    if os.path.exists(file):
        print(os.path.basename(file))


# with open(r"C:\Users\14058\OneDrive\Desktop\Programming\Python Stuff\PDFs\PdfPages\dummy.pdf", "rb") as new_file:
#     reader = PyPDF2.PdfFileReader(new_file)
#     first_page = reader.getPage(0)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(first_page)
#     with open(r"C:\Users\14058\OneDrive\Desktop\Programming\Python Stuff\PDFs\PdfPages\twopage.pdf", "wb") as new_file2:
#         writer.write(new_file2.getPage(0))
#         writer.write(new_file2.getPage(1))
#         new_writer = PyPDF2.PdfFileWriter()
#         new_writer.addPage(writer)
#         with open(r"C:\Users\14058\OneDrive\Desktop\Programming\Python Stuff\PDFs\PdfPages\new_dummy.pdf", "wb") as new_file3:
#             new_writer.write(new_file3)
#             page_one = new_file3.getPage(0)
#             new_writer.addPage(page_one)
#             combined_writer = PyPDF2.PdfFileWriter()
#             combined_writer.addPage(new_writer)
#             with open(r"C:\Users\14058\OneDrive\Desktop\Programming\Python Stuff\PDFs\PdfPages\combined.pdf", "wb") as combined:
#                 combined_writer.write(combined)

def pdf_combiner(pdf_list):
    try:
        merger = PyPDF2.PdfFileMerger()
        for idx, pdf in enumerate(pdf_list):
            merger.append(pdf)
        with open(r"C:\Users\14058\OneDrive\Desktop\Programming\Python Stuff\PDFs\PdfPages\combined.pdf", "wb") as combined:
            merger.write(combined)

    except FileNotFoundError as err:
        print(err)


# add watermark to all pages in combined file

combined_file = PyPDF2.PdfFileReader(open(
    r"C:\Users\14058\OneDrive\Desktop\Programming\Python Stuff\PDFs\PdfPages\combined.pdf", "rb"))
watermark_file = PyPDF2.PdfFileReader(open(
    r"C:\Users\14058\OneDrive\Desktop\Programming\Python Stuff\PDFs\PdfPages\wtr.pdf", "rb"))
combined_watermark = PyPDF2.PdfFileWriter()


def add_wtr():
    for i in range(combined_file.getNumPages()):
        indiv_page = combined_file.getPage(i)
        # adds 1st page of watermark to each page in combined file
        indiv_page.mergePage(watermark_file.getPage(0))
        # adding them all to the writer object
        combined_watermark.addPage(indiv_page)

    with open(r"C:\Users\14058\OneDrive\Desktop\Programming\Python Stuff\PDFs\PdfPages\combined_watermark.pdf", "wb") as com_wtr:
        # writing contents of writer file to new file
        combined_watermark.write(com_wtr)

# if __name__ == '__main__':
#     pdf_combiner(file_inputs)
