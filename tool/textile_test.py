#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

# Add textile and pygments into python lib path
lib = os.path.abspath('.')
sys.path.append(lib)

import textile

def getContent(fileName):
    article = open(fileName, 'r')
    s = "".join(article.readlines())
    s.replace("\r","")
    return s

if __name__ == '__main__':
    if sys.argv.__len__() > 1:
        s = getContent(sys.argv[1])
        html = textile.textile(s)
        #print html
    else:
        print 'no input file!!!'
