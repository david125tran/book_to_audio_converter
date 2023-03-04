#----------------------------------------Terminal Installations----------------------------------------#
# pip install gTTS
# pip install pypdf2
# pip install mutagen

#----------------------------------------Imports----------------------------------------#
from gtts import *
import os
import PyPDF2
from mutagen.mp3 import MP3

#--------------------------------------Open The PDF-------------------------------------#
filename = "pdf_file.pdf"
pdf = open(filename, 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf)

#-----------------------------Get The Total Number of Pages-----------------------------#
total_pages = pdf_reader.numPages

#-----------------------------------Extract The Text------------------------------------#
text = ""
for page_number in range(0, total_pages):
    # Extract the text from each page
    new_page = pdf_reader.getPage(page_number)
    new_page_text = new_page.extractText()
    text = text + "\n\n" + new_page_text  # Add the text to the previous pages if there are any

print("\npdf being extracted to audio, hang tight...")

# -----------------------------------Convert the text to mp3 audio------------------------------------#
audio = gTTS(text=text, lang='en', slow=False)
# Each page becomes a new file
audio.save("audio.mp3")

# -----------------------------------Play the Speech------------------------------------#
os.system("audio.mp3")
print(text)






