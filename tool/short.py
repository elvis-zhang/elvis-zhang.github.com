#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib

# This algorithm is from :
#   http://www.snippetit.com/2009/04/php-short-url-algorithm-implementation/
base32 = (
"a","b","c","d","e","f","g","h",
"i","j","k","l","m","n","o","p",
"q","r","s","t","u","v","w","x",
"y","z","0","1","2","3","4","5")

def mapping(origin):
    key = "aluckyapple.github.com"
    md5Hex = hashlib.md5(key + origin).hexdigest()
    res = [0 for i in range(4)]
    for i in range(4):
        intval = 0x3FFFFFFF & int("0x" + md5Hex[i * 8: i * 8 + 8], 16)
        output = ""
        for j in range(6):
		    index = 0x0000001F & intval
		    output += base32[index]
		    intval = intval >> 5
        res[i] = output
    return res

if __name__ == '__main__':
    print mapping('https://www.google.com.hk')
