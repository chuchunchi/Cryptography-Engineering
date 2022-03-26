# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 17:17:09 2022

@author: chuch
"""

text = "ECDTM  ECAER   AUOOL EDSAM  MERNE  NASSO DYTNR  VBNLC  RLTIQ \
LAETR   IGAWE  BAAEI HOR"


def counting(n,m):
    vowel = [0]*n
    j=0
    for i in text :
        if i != " ":
            if(j==n):
                j=0
            if i=='A'or i=='E' or i=='I' or i=='O' or i=='U':
                vowel[j]+=1
            j+=1
    
    ans1=0
    for i in range(n):
        ans1+=abs(vowel[i]-m*0.4)
        
    print(ans1)
    return ans1
    
a1=counting(7,9)
a2=counting(9,7)
if(a1>a2):
    print("the dimension is 9*7")
elif(a2>a1):
    print("the dimension is 7*9")