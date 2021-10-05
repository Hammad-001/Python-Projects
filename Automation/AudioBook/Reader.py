# importing text-to-speach and pdf and system
import pyttsx3, PyPDF2, sys

def pdfReader(book_path, start_page=0, uptil_page=-1):
    # opening book 
    # first argument is path of the book and second is type read binary 
    book = open(book_path, "rb")

    # to use pypdf to create file reader for the book
    Reader = PyPDF2.PdfFileReader(book)

    # get page numbers
    book_pages = Reader.numPages

    if uptil_page == -1:
        uptil_page = book_pages
    # initialize variable of text to speech
    speaker = pyttsx3.init()

    # loop to read every page from pdf
    # start_page-1 because in programming pages start from 0
    for page_nums in range(start_page-1, uptil_page):
        
        # get every page from pdf
        get_page = Reader.getPage(page_nums)
        
        # extracting text from page
        page_text = get_page.extractText()
        
        # making speaker to read
        speaker.say(page_text)
        
        # run speaker
        speaker.runAndWait()

pdfReader("D:\\Study\\Semester\\Semester 5\\Electronics 1\\data\\Electronic Devices 9th Edition by Floyd.pdf", 29 ,30)