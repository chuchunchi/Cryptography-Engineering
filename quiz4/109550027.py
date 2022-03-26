# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 19:58:52 2022

@author: chuch
"""
import string
import math
text = "EOEYE GTRNP SECEH HETYH SNGND DDDET OCRAE RAEMH\
TECSE USIAR WKDRI RNYAR ANUEY ICNTT CEIET US"
plaintextref = "WITHM ALICE TOWAR DNONE WITHC HARIT YFORA LLWIT\
HFIRM NESSI NTHER IGHTA SGODG IVESU STOSE ETHERIGHTL ETUSS TRIVE ONTOF INISH THEWO RKWEA REINT\
OBIND UPTHE NATIO NSWOU NDSTO CAREF ORHIM WHOSHALLHA VEBOR NETHE BATTL EANDF ORHIS WIDOW ANDHI\
SORPH ANTOD OALLW HICHM AYACH IEVEA NDCHE RISHAJUSTA NDLAS TINGP EACEA MONGO URSEL VESAN DWITH\
ALLNA TIONS GREEC EANNO UNCED YESTE RDAYT HEAGRAGREE MENTW ITHTR UKEYE NDTHE CYPRU STHAT THEGR\
EEKAN DTURK ISHCO NTING ENTSW HICHA RETOP ARTICIPATE INTHE TRIPA RTITE HEADQ UARTE RSSHA LLCOM\
PRISE RESPE CTIVE LYGRE EKOFF ICERS NONCO MMISSIONED OFFIC ERSAN DMENA NDTUR KISHO FFICE RSNON\
COMMI SSION EDOFF ICERS ANDME NTHEP RESID ENTANDVICE PRESI DENTO FTHER EPUBL ICOFC YPRUS ACTIN\
GINAG REEME NTMAY REQUE STTHE GREEK ANDTU RKISHGOVER NMENT STOIN CREAS EORRE DUCET HEGRE EKAND\
TURKI SHCON TINGE NTSIT ISAGR EEDTH ATTHE SITESOFTHE CANTO NMENT SFORT HEGRE EKAND TURKI SHCON\
TINGE NTSPA RTICI PATIN GINTH ETRIP ARTIT EHEADQUART ERSTH EIRJU RIDIC ALSTA TUSFA CILIT IESAN\
DEXEM PTION SINRE SPECT OFCUS TOMSA NDTAX ESASWELLAS OTHER IMMUN ITIES ANDPR IVILE GESAN DANYO\
THERM ILITA RYAND TECHN ICALQ UESTI ONSCO NCERNINGTH EORGA NIZAT IONAN DOPER ATION OFTHE HEADQ\
UARTE RSMEN TIONE DABOV ESHAL LBEDE TERMI NEDBYASPEC IALCO NVENT IONWH ICHSH ALLCO MEINT OFORC\
ENOTL ATERT HANTH ETREA TYOFA LLIAN CE"
d3={}
d2={}
def markov():
    plain = plaintextref.translate({ord(c): None for c in string.whitespace})
    #print(plain)

    for i in range(len(plain)-2):
        j=i+1
        k=i+2
        temp=""
        temp+=plain[i]
        temp+=plain[j]
        temp+=plain[k]
        if temp in d3:
            d3[temp]+=1
        else:
            d3[temp]=1

    #print(d3)
    for i in range(len(plain)-1):
        j=i+1
        temp=""
        temp+=plain[i]
        temp+=plain[j]
        if temp in d2:
            d2[temp]+=1
        else:
            d2[temp]=1

    #print(d2)
        
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
        
    #print(ans1)
    return ans1

n1=7
m1=11
n2=11
m2=7
if counting(n1,m1)>counting(n2,m2):
    n=n2
    m=m2
else:
    n=n1
    m=m1
print(n,"*",m)
markov()
strcol=[""]*m
ind=0
c=0
for t in text:
    if c==n:
        c=0
        ind+=1
    if t != " ":
        strcol[ind]+=t
        c+=1
'''for i in range(m):
    print(strcol[i])'''
firstcol = 2
seccol = 5
ndone = [0,1,2,3,4,5,6]
resultcol=[firstcol,seccol]
ndone.remove(firstcol)
ndone.remove(seccol)

for i in range(2,m):
    maxprob=0
    choosecol=-1
    for j in ndone:
        probs=0
        for w in range(m):
            char2=""
            char2 += strcol[firstcol][w]
            char2 += strcol[seccol][w]
            
            char3 = char2+strcol[j][w]
            if char2 not in d2 or char3 not in d3:
                continue
            else:
                probs+=math.log(26*(d3[char3]/d2[char2]))
        if probs>maxprob:
            
            maxprob=probs
            choosecol=j
    ndone.remove(choosecol)
    resultcol.append(choosecol)
    firstcol=seccol
    seccol=choosecol

plaintext=""
for i in range(n):
    for col in resultcol:
        plaintext+=strcol[col][i]
print(plaintext)