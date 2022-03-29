# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 20:42:16 2022

@author: chuch
"""

import hashlib

md = hashlib.md5()
data=input()
db = bytes.fromhex(data)
md.update(db)
hexi=md.hexdigest()
print(hexi[:4])


num=0
while(1):
    hnum=format(num,'x')
    hnum = hnum.zfill(32)
    barr=bytes.fromhex(hnum)
    md1 = hashlib.md5()
    md1.update(barr)
    h=md1.hexdigest()
    if h[:4]==hexi[:4]:
        print(hnum)
        break
    num+=1