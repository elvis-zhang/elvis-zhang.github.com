#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
# Add textile and pygments into python lib path
lib = os.path.abspath('.')
sys.path.append(lib)

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

if __name__ == '__main__':
    s = '''
    public class Building
    {   
        private int no = 0; 
        private boolean f = false;
        public void who()
        {
            System.out.println("I am a lucky apple.");
        }
    }
    '''
    lexer = get_lexer_by_name("java")
    formatter = HtmlFormatter(full=True, linenos=True, noclasses=True, outencoding='utf-8')

    html = highlight(s, lexer, formatter)
    print html
