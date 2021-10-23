from pyPDF2 import PdfFileWriter, PdfFileReader


def pdf_merger(file1, file2, start_from, merged):
    main_file = PdfFileReader(file1, 'rb')
    file_to_be_merged = PdfFileReader(file2, 'rb')
    output = PdfFileWriter()

    for i in range(main_file.getNumPages()):
        output.addPage(main_file.getPage(i))
        if i == start_from:
            for page in range(file_to_be_merged.getNumPages()):
                output.addPage(file_to_be_merged.getPage(page))

    with open(merged, 'wb') as f:
        output.write(f)


if __name__ == '__main__':
    file1 = input('Enter the path of the file to be merged to ==> ')
    file2 = input('\nEnter the path of the file to be merged ==> ')
    start_from = input('\nEnter the page where you want to start merging ==> ')
    pdf_merger(file1, file2, start_from, merged='merged_file.pdf')
