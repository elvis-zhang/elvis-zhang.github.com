#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

# Add textile and pygments into python lib path
lib = os.path.abspath('.')
sys.path.append(lib)

import textile
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

def getContent(fileName):
    article = open(fileName, 'r')
    lineList = article.readlines()
    sep = '```'

    # Get the positions of the code snippets
    sepPosition = []
    idx = 0
    for line in lineList:
        if line.startswith(sep):
            #print line
            sepPosition.append(idx)
        idx += 1

    # Get the code snippets and the code type
    codeSnip = []
    codeType = []
    for i in range(len(sepPosition) / 2):
        codeSnip.append(lineList[sepPosition[i * 2] + 1 : sepPosition[i * 2 + 1]])
        codeType.append(lineList[sepPosition[i * 2]].replace(sep,'').replace('\n',''))
        for j in range(sepPosition[i * 2 + 1] - sepPosition[i * 2] + 1):
            j += sepPosition[i * 2]
            if j == sepPosition[i * 2]:
                lineList[j] = sep
            elif j == sepPosition[i * 2 + 1]:
                lineList[j] = '\n'
            else:
                lineList[j] = ''

    # Use pygments to translate code to html 
    formatter = HtmlFormatter(linenos=True, noclasses=True, outencoding='utf-8')
    for i in range(len(codeSnip)):
        lexer = get_lexer_by_name(codeType[i])
        codeSnip[i] = highlight(''.join(codeSnip[i]), lexer, formatter)
      
    #print codeSnip

    # use textile to parse textile code
    contentNoCode = ''.join(lineList)
    htmlCandidate = textile.textile(contentNoCode)

    # insert code snippets into the candidate html
    for s in codeSnip:
        htmlCandidate = htmlCandidate.replace(sep, s, 1)
    
    return htmlCandidate

if __name__ == '__main__':
  if sys.argv.__len__() > 1:
      s = getContent(sys.argv[1])
      print s
  else:
      print 'no input file!!!'
