#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Template:
    __TEMPLATE_START = "{{"  
    __TEMPLATE_END = "}}"  
    
    def __init__(self, startToken = "{{", endToken = "}}"):
        """
        The default startToken is "{{" and endToken is "}}". You can use
        any token you like.
        Notice: The first charactor after startToken must not be '#'. '#'
                is reserved here. The expression after '#' will be called 
                by eval().
        """
        self.__TEMPLATE_START = startToken
        self.__TEMPLATE_END = endToken

    def compile(self, tpl):
        templateC = []  
        snippets = []  
        current = 0  
        while True:
            start = tpl.find(self.__TEMPLATE_START, current)  
            sBegin = start + len(self.__TEMPLATE_START)
            sEnd = tpl.find(self.__TEMPLATE_END, sBegin) 

            if sBegin >= len(self.__TEMPLATE_START) and sEnd > sBegin:
                templateC.append(tpl[current:start]) 
                sn = tpl[sBegin:sEnd]  
                if sn.find('#') == 0:
                    sn = eval(sn[1:])  
                else:
                    snippets.append(len(templateC))  
                templateC.append(sn)  
            else:
                templateC.append(tpl[current:])  
                break 

            current = sEnd + len(self.__TEMPLATE_END)
            # while loop end

        templateC.append(snippets)  
        return templateC  

    def __doFillData(self, data, sn):
        """
        This is the default render method. Just fill the keyword with data.
        """
        return eval('data["' + sn + '"]')

    def render(self, templateC, data, method = None):
        if method == None:
            method = self.__doFillData

        snippets = templateC[len(templateC) - 1]  
        rs = []  
        sIdx = 0  

        for i in range(len(templateC) - 1): 
            if sIdx < len(snippets) and snippets[sIdx] == i:  
                rs.append(method(data, templateC[i]))  
                sIdx += 1
            else:   
                rs.append(templateC[i])
        #import sys
        #reload(sys) 
        #sys.setdefaultencoding('utf8') 
        return "".join(rs)     
 	 
    def compileAndRender(self, tpl, data, method = None):
        tc = self.compile(tpl)
        return self.render(tc, data, method)

if __name__ == '__main__':
    tpl = "<title>{{title}}</title><body>{{content}}</body>"
    data = {}
    data['title'] = 'This is title'
    data['content'] = 'This is a simple template engine for 1-D array'
    t = Template()
    out = t.compileAndRender(tpl, data)
    print out
