import PyPDF2
from gtts import gTTS
from functools import lru_cache
import os

@lru_cache(maxsize=1000)
def pdfToTxt(pdfFileName,pageNum):
    pdfFile = open("coders-at-work.pdf","rb") 
    readPdf = PyPDF2.PdfFileReader(pdfFile)
    pageNo = readPdf.getPage(pageNum)
    readPage = pageNo.extractText()
    return readPage

def textToSpeech(pdfName):
    text = pdfToTxt('coders-at-work.pdf',60)
    language = 'en'
    readText = gTTS(text=text,lang=language,slow=False)
    file_name = f"{pdfName}toAudio.mp3"
    readText.save(file_name)
    os.system(file_name)

if __name__ == "__main__":
    print("Generating Pdf to Text")
    print(pdfToTxt('coders-at-work.pdf',60))
    print("Done Generating Pdf to text ... Now generating Text to speech")
    textToSpeech('coders-at-work')
    