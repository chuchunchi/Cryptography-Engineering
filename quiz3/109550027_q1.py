# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 22:52:59 2022

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

    
ans = [0]*4
text = input()
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
    #print(abs(total/i-0.066))
print(ans.index(min(ans))+4)