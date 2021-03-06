#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import getopt
from subprocess import call

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD =  '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def mainWithNoArgs():
    searchWord = input('Enter the word you want to search (Default : "//TODO") : ')
    if not searchWord:
        searchWord = "//TODO"

    isInputPathEmpty = True
    inputPath = input('{0}Enter the path of your file \nEx : /home/myHome/Desktop/myFile/ \nPath (Enter for Default:working directory) : '.format(color.BOLD))
    if not inputPath:
        os.system('pwd')
        os.system('ls')
        isInputPathEmpty = True
    else:
        os.chdir(inputPath)
        os.system('pwd')
        os.system('ls')
        isInputPathEmpty = False

    inputFileName = input('{0}Enter your file name \nEx : example.txt \nFile name : '.format(color.BOLD))
    if isInputPathEmpty is True:
        inputFilePath = inputFileName
    else:
        inputFilePath = inputPath+'/'+inputFileName


    isOutputPathEmpty = True
    outputPath = input('{0}Enter the path of you want to extract file \nEx : /home/myHome/Desktop/myFile/ \nPath : '.format(color.BOLD))
    if not outputPath:
        os.system('pwd')
        os.system('ls')
        isOutputPathEmpty = True
    else:
        os.chdir(outputPath)
        os.system('pwd')
        os.system('ls')
        isOutputPathEmpty = False

    outputFileName = input('{0}Enter your file name of you want to extract \nEx : example.txt \nFile name : '.format(color.BOLD))
    if isOutputPathEmpty is True:
        outputFilePath = outputFileName
    else:
        outputFilePath = outputPath+'/'+outputFileName

    inputFile = open(inputFilePath,"r",encoding="utf-8")
    outputFile = open(outputFilePath,"a",encoding="utf-8")
    inputLine = inputFile.readline()
    while inputLine:
        if (inputLine.startswith(searchWord) == 1):
            head, inputText = inputLine.split(searchWord)
            outputFile.writelines(inputText)
        inputLine = inputFile.readline()

    inputFile.close() #inputFile closed
    outputFile.close() #outputFile closed

def commandLineSearch(inputFileArg,outputFileArg,searchWordArg):
    print("input : "+inputFileArg)
    print("output : "+outputFileArg)
    print("searchWord : "+searchWordArg)
    inputFile = open(inputFileArg,"r",encoding="utf-8")
    outputFile = open(outputFileArg,"a",encoding="utf-8")
    inputLine = inputFile.readline()
    while inputLine:
        if (inputLine.startswith(searchWordArg) == 1):
            head, inputText = inputLine.split(searchWordArg)
            outputFile.writelines(inputText)
        inputLine = inputFile.readline()

    inputFile.close() #inputFile closed
    outputFile.close() #outputFile closed
    print("Successful!")
    sys.exit()

def searchWordDefault(inputFileArg,outputFileArg):
    print("input : "+inputFileArg)
    print("output : "+outputFileArg)
    searchWord = '//TODO'
    inputFile = open(inputFileArg,"r",encoding="utf-8")
    outputFile = open(outputFileArg,"a",encoding="utf-8")
    inputLine = inputFile.readline()
    while inputLine:
        if (inputLine.startswith(searchWord) == 1):
            head, inputText = inputLine.split(searchWord)
            outputFile.writelines(inputText)
        inputLine = inputFile.readline()

    inputFile.close() #inputFile closed
    outputFile.close() #outputFile closed
    print("Successful!")
    sys.exit()


def usage():
    print("usage: python3.5 main.py -i <inputFile> -o <outputFile> -s <searchWord>")

def main(argv):
   inputfile = ''
   outputfile = ''
   searchword = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:s:",["ifile=","ofile=","sword="])
   except getopt.GetoptError:
      usage()
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-h","--help"):
         usage()
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      elif opt in ("-s", "--sword"):
         searchword = arg
   commandLineSearch(inputFileArg=inputfile,outputFileArg=outputfile,searchWordArg=searchword)
   #searchWordDefault(inputFileArg=inputfile,outputFileArg=outputfile)

if __name__ == "__main__":
    main(sys.argv[1:]) #Calling main
