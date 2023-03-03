#----------------------------------------Imports----------------------------------------#
from gtts import *
import os
import PyPDF2
# pip install gTTS
# pip install pypdf2
import time
from mutagen.mp3 import MP3


#--------------------------------------Open The PDF-------------------------------------#
pdf = open("pdf_file.pdf", 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf)

#-----------------------------Get The Total Number of Pages-----------------------------#
total_pages = pdf_reader.numPages

#-----------------------------------Extract The Text------------------------------------#
print("\npdf being extracted to audio, hang tight...")

for page_number in range (0, total_pages):
    # Extract the text from each page
    new_page = pdf_reader.getPage(page_number)
    new_page_text = new_page.extractText()
    # Convert the text to speech (.mp3 file)
    new_page_speech = gTTS(text=new_page_text, lang='en', slow=False)
    # Each page becomes a new file
    new_page_speech.save(f"new_page_speech_{page_number}.mp3")

print("\nText extraction complete.  Audio opening...")

#-----------------------------------Play the Speech------------------------------------#
for page_number in range (0, total_pages):
    os.system(f"new_page_speech_{page_number}.mp3")
    audio = MP3(f"new_page_speech_{page_number}.mp3") # Extract the length of the mp3 of the page
    time.sleep(int(audio.info.length) + 2) # Wait for the mp3 of the page to finish playing before looping to
    # the next page








