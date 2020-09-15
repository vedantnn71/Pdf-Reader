summaryOfThisProduct =
{
    'product name': 'Pdf reader',
    'type': 'software',
    'cost': 0,
    'version': '1.1.0',
    'description': 'To use this software you must be connected to internet , this software is used to make pdf to speech , for more info contact at vedantnn.confidentail@gmail.com',
    'Author': 'Vedant Nandwana'
}

import PyPDF2
from functools import lru_cache
from gtts import gTTS
from playsound import playsound

# variables and inputs
fileName = input("Enter The Name of Pdf *Do not enter .pdf*\n")
filePageNumber = int(input("Enter The Page Number of Pdf\n"))
audio_name = f"{fileName}toAudio.mp3"

"""
This Function Converts Pdf to Text (This FUnction is called 2 times)
Cache Is Set in a Large amount To increase the efficency and Readable Lines
"""
@lru_cache(maxsize=10000000)
def pdfToTxt(pdfFileName,pageNum):
    try:
        _pdfName = pdfFileName+'.pdf'
        _pdfFile = open(_pdfName,"rb") 
        _readPdf = PyPDF2.PdfFileReader(_pdfFile)
        _pageNo = _readPdf.getPage(pageNum)
        _readPage = _pageNo.extractText()
        return _readPage
    except FileNotFoundError:
        print("Invalid File Name Enter The Correct One")

"""
This fucntion Makes a File Converted into txt
"""
def mkPdfToTxtFile(pdfFile_name,pgNum):
    readPdfFile = pdfToTxt(pdfFile_name,pgNum)
    txtFileName = pdfFile_name+".txt"
    txtFileOfPdf = open(txtFileName,'w+')
    txtFileOfPdf.write(readPdfFile)
    txtFileOfPdf.write("Thanks For Using Pdf to speech and text")
    readThePdf = txtFileOfPdf.read()
    txtFileOfPdf.close()
    return readThePdf

'''
This function converts pdf's text into audio
'''
def textToSpeech(pdfName,pageNum):
    text = pdfToTxt(pdfName,pageNum)
    language = 'en'
    readText = gTTS(text=text,lang=language,slow=False)
    file_name = f"{pdfName}toAudio.mp3"
    readText.save(file_name)

'''
This function checks the operating system and then speaks according to it
'''


if __name__ == "__main__":
    print("Generating Pdf to Text")
    print(pdfToTxt(fileName,filePageNumber))

    print(f"Done Generating Pdf to Text ... Now Creating a txt file with name {fileName}.txt")
    mkPdfToTxtFile("coders-at-work",filePageNumber)

    print(f"\nDone Creation of {fileName}.txt file ... Now generating Text to speech Please Wait This May Take A While..")
    textToSpeech(fileName,filePageNumber)

    print("Done Creation of Text To Speech ... Now Playing Audio")
    # checkAndPlay(audio_name)  
    playsound(audio_name)

    print(f"Done Creation of 2 files with name {fileName}.txt and {fileName}.mp4 and Successfully Played The Audio\nThanks For using Pdf To Speech and text program")
    a = input("Press enter to exit")
    # This is to not exit()
