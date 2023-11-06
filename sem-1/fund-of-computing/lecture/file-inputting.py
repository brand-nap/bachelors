from tkinter import *
from tkinter.filedialog import askopenfilename

def main():
    print("PLease choose the file with names and grades in it: ")
    inputFileName = askopenfilename()
    print("file name is ==> ", inputFileName)
    processFile(inputFileName)

def processFile(fileName):
    inFile = open(fileName, "r")
    line = inFile.readline();
    while line != "":
        print(line)
        line = line = inFile.readline();
    inFile.close()

main()
