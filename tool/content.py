#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

# Add textile and pygments into python lib path
lib = os.path.abspath('.')
sys.path.append(lib)

from template import Template
import textile
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

def parse(content):
    sep = "```"
    t = Template(sep, sep)
    tc = t.compile(content) # Template compiled
    snp = tc[len(tc) - 1] # Get all snippets position
    
    # Highlight the snippets
    # Flush the snippets for textile
    sn = []
    snl = [] # Snippet language type
    for i in range(len(snp)):
        tidx = tc[snp[i]].find('\n') # Find the first \n to find language type
        snl.append(tc[snp[i]][:tidx])
        sn.append(tc[snp[i]][tidx + 1:])
        tc[snp[i]] = sep + str(i) + sep
    
    # Use pygments to highlight the code snippets
    formatter = HtmlFormatter(linenos=True, noclasses=True, outencoding='utf-8')
    for i in range(len(sn)):
        lexer = get_lexer_by_name(snl[i])
        sn[i] = highlight("".join(sn[i]), lexer, formatter)
    
    textileContent = "".join(tc[:-1])
    htmlCandidate = textile.textile(textileContent)

    # Compile again to fill the highlighted code snippet to the the whole html
    tc = t.compile(htmlCandidate) # Template compiled
    return t.render(tc, sn, lambda d,i:d[int(i)])

def fill(data, tpl):
    t = Template()
    return t.compileAndRender(tpl, data)
    

if __name__ == '__main__':
    if sys.argv.__len__() > 1:
        fileName = sys.argv[1]
        article = open(fileName, 'r')
        content = "".join(article.readlines())
        p = parse(content)
        print p
    else:
        print 'no input file!!!'
