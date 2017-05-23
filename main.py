#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
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

inputPath = input('{0}Enter the path of your file \nEx : /home/myHome/Desktop/myFile/ \nPath : '.format(color.BOLD))

os.chdir(inputPath)
os.system('pwd')
os.system('ls')



inputFileName = input('{0}Enter your file name \nEx : example.txt \nFile name : '.format(color.BOLD))
inputFilePath = inputPath+'/'+inputFileName
inputFile = open(inputFilePath,"r",encoding="utf-8")

inputLine = inputFile.readline()
while inputLine:
    if (inputLine.startswith("//TODO") == 1):
        head, inputText = inputLine.split("//TODO")
        print(inputText)
    inputLine = inputFile.readline()
inputFile.close()


