# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 15:01:53 2022

@author: chuch
"""

test_str = "K YZWLNKXKJWGN QUGN ETNMX MPLMZOMXYM K TMMJOXA XEN TKZ ZMQEBMF TZEQ\
KJKZQ EX KXKJWDOXA KXF MPLJEZM NHM TJEEF ET XMI CXEIJMFAM IHOYH MKYH WMKZ RZOXAG IONH ON"
  
freq = {}
for i in test_str:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
  
print (str(freq))