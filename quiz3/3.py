# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 23:11:57 2022

@author: chuch
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 23:44:53 2022

@author: chuch
"""

def IC(text):
    freq = {}
    for i in text:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    strlen = len(text)
    ans=0
    for ch, f in freq.items():
        if(f>=1 and strlen>1):
            ans+=(f*(f-1)/strlen/(strlen-1))
    #print(ans)
    return ans

engfreq = {'A':8.167, 'B':1.492, 'C':2.782, 'D':4.253,'E':12.702, 'F':2.228, \
           'G':2.015, 'H':6.094,'I':6.966,'J':0.153, 'K':0.772, 'L':4.025,\
            'M':2.406, 'N':6.749, 'O':7.507, 'P':1.929,'Q':0.095, 'R':5.987,\
            'S':6.327, 'T':9.056,'U':2.758, 'V':0.978, 'W':2.36, 'X':0.15, 'Y':1.974, 'Z':0.074}

while(1):
    ans = [0]*4
    text = input("enter text: ")
    for i in range(4,8):
        tstr = [""]*i
        num=0
        for t in text:
            if(num==i):
                num=0
            tstr[num]+=t
            num+=1
        total=0
        for ind in range(i):
            total+=IC(tstr[ind])
        ans[i-4] = abs(total/i-0.066)
    keylen = ans.index(min(ans))+4
    #end of q1
    #start of q2
    tstr = [""]*keylen
    num=0
    for t in text:
        if(num==keylen):
            num=0
        tstr[num]+=t
        num+=1
    print(tstr)
    print(chr(ord('Z')+ord('H')-ord('A')),ord('Z'),ord('B'),ord('A'))
    nts = [""]*6
    key = ['P','O','I','R','O','T']
    for i in range(keylen):
        for w in tstr[i]:
            if (ord(w)-ord(key[i])+ord('A'))<65:
                nts[i]+=chr(ord(w)-ord(key[i])+ord('A')+26)
            else:
                nts[i]+=chr(ord(w)-ord(key[i])+ord('A'))
    l=0
    lennn=""
    print(nts)
    while(l<len(nts[0])):
        #print(l)
        for i in range(6):
            if(l<len(nts[i])):
                lennn+=nts[i][l]
                #print(nts[i][l])
        l+=1
    print(lennn)
        
        
        
        