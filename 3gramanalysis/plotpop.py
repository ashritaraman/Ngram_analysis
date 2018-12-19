#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 21:05:48 2018

@author: ashritaraman
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 23:27:51 2018

@author: ashritaraman
"""
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from collections import Counter
from collections import defaultdict
from operator import itemgetter
import itertools
import operator
import numpy as np
from scipy.interpolate import splrep, splev


sns.set(style="white", palette="muted", color_codes=True)
with open('3gramuglydataset.csv') as fin, open('3gramnicedataset.csv', 'w') as fout:
    for line in fin:
        fout.write(line.replace('\t', ','))
        
x = []
y = []

x1 = []
y1 = []

fx = []
fy = []

fx1 = []
fy1 = []

fx2 = []
fy2 = []

numarray = []
freqdict = {} #for -1 -1 -2
freqdict1 = {} #for -1 -1 2
freqdict2 = {} #for -1 -2 0
freq1900top20 = {}
freqall = {}

with open('3gramnicedataset.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    cnt = Counter()
    popngram = Counter()
    cntyr = Counter()
    for row in plots:
        #counter for total # of ngrams in a year
        year = int(row[3])
        cnt[year] += int(row[4]) 
        cntyr[year] +=1 #most frequent year
        s = row[0] + row[1] + row[2]
        numarray.append(s)
        
    

#open csv file again to read a second time
with open('3gramnicedataset.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        #s is the ngram
        s = row[0] + row[1] + row[2]
        numarray.append(s)
        if (s == '-1-2-2'):
            occ = int(row[4])
            freqdict[int(row[3])] = occ/cnt.get(int(row[3])) 
        elif (s == '-1-22'):
            occ = int(row[4])
            freqdict1[int(row[3])] = occ/cnt.get(int(row[3])) 
        elif (s == '-1-20'):
            occ = int(row[4])
            freqdict2[int(row[3])] = occ/cnt.get(int(row[3]))       
        if (int(row[3]) == 1900):
            occ = int(row[4])
            if (occ > 300):  
                freq1900top20[s] = occ/cnt.get(int(row[3])) 
                
                   
for i in range (1800,2000):
    if i in freqdict:
        fx.append(i)
        fy.append(freqdict.get(i))
    else:
        fx.append(i)
        fy.append(0)
        
for i in range (1800,2000):
    if i in freqdict1:
        fx1.append(i)
        fy1.append(freqdict1.get(i))
    else:
        fx1.append(i)
        fy1.append(0)
        
for i in range (1800,2000):
    if i in freqdict2:
        fx2.append(i)
        fy2.append(freqdict2.get(i))
    else:
        fx2.append(i)
        fy2.append(0)
        

#smoothed graph for -1-2-2      
bspl = splrep(fx, fy, s = 0)
x_smooth = np.linspace(min(fx), max(fx), 50)
bspl_y = splev(x_smooth, bspl)
plt.figure()
plt.plot(x_smooth, bspl_y, label = 'Frequency of -1 -2 -2 ngram')   
plt.title('Frequency of -1 -2 -2 ngram')
plt.xticks(fontsize = 10)
plt.xlabel('year')
plt.ylabel('frequency')
plt.yticks(fontsize = 10)
plt.legend()
plt.show()

#unsmoothed graph for -1 -2 -2
plt.plot(fx, fy, label = 'No smoothing')
plt.xlabel('year')
plt.ylabel('frequency')
plt.title('Frequency of -1 -2 -2 ngram without smoothing')
plt.legend()
plt.show()

#smoothed graph for -1-2 2
bspl1 = splrep(fx1, fy1, s = 0)
x_smooth1 = np.linspace(min(fx1), max(fx1), 50)
bspl_y1 = splev(x_smooth1, bspl1)
plt.figure()
plt.plot(x_smooth1, bspl_y1, label = 'Frequency of -1 -2 2 ngram')   
plt.title('Frequency of -1 -2 2 ngram')
plt.xticks(fontsize = 10)
plt.xlabel('year')
plt.ylabel('frequency')
plt.yticks(fontsize = 10)
plt.legend()
plt.show()

#unsmoothed graph for -1 -2 2
plt.plot(fx1, fy1, label = 'No smoothing')
plt.xlabel('year')
plt.ylabel('frequency')
plt.title('Frequency of -1 -2 2 ngram without smoothing')
plt.legend()
plt.show()

#smoothed graph for -1-20  
bspl2 = splrep(fx2, fy2, s = 0)
x_smooth2 = np.linspace(min(fx2), max(fx2), 50)
bspl_y2 = splev(x_smooth2, bspl2)
plt.figure()
plt.plot(x_smooth2, bspl_y2, label = 'Frequency of -1-2 0 ngram')   
plt.title('Frequency of -1-2 0 ngram')
plt.xticks(fontsize = 10)
plt.xlabel('year')
plt.ylabel('frequency')
plt.yticks(fontsize = 10)
plt.legend()
plt.show()

#unsmoothed graph for -1 -2 0
plt.plot(fx2, fy2, label = 'No smoothing')
plt.xlabel('year')
plt.ylabel('frequency')
plt.title('Frequency of -1 -2 0 ngram without smoothing')
plt.legend()
plt.show()




            

testlist = []    
#trying to get frequency of all ngrams
with open('3gramnicedataset.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        #s is the ngram
        s = row[0] + row[1] + row[2]
        occ = int(row[4])
        testlist.append([s, int(row[3]),occ/cnt.get(int(row[3]))])
        occ = int(row[4])
        freqall[s] = (int(row[3]), occ/cnt.get(int(row[3])))
     
numarray.append(s)
occ = int(row[4])
freqdict[s] = occ/cnt.get(int(row[3]))


        
#creates a dictionary with the years and the total number
#of occurrences
#if yr in freqdict:
#    freqdict[yr] = int(freqdict[yr]) + int(occ)
#else:
#    freqdict[yr] = int(occ)
print("NUMARRAY")
print(numarray)
print("COUNTER")
print(cnt)
print(freqdict)
dictarray = Counter(numarray)
print('dictarray')
print(dictarray)
print("MOST COMMON")
print(freq1900top20)
##
##
for i, (key, val) in enumerate(dictarray.most_common()):
    x.append(i)
    y.append(val)
#    
#    
sortedar = sorted(freq1900top20.items(), key=itemgetter(1), reverse =True)
#print(sortedar)
first,snd = zip(*sorted(sortedar))
plt.plot(first,snd, label='Frequency of all ngrams')
plt.xticks(rotation=90)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Frequency of ngrams in 1900 with occurrency > 300')
plt.legend()
plt.show() 
###
#sorteddictarray = sorted(dictarray.items(), key=itemgetter(1), reverse =True)
##print(sorteddictarray)
#
#for elt in range (1, 20):
#    felt = sorteddictarray[elt]
#    x1.append(felt[0])
#    y1.append(felt[1])
#
##maxelt = max(sorteddictarray, key=sorteddictarray.get)
##print(maxelt)
#
#x1, y1 = zip(*sorted(zip(x1, y1)))
#plt.xticks(rotation=90)
#print(x1)
#print(y1)
#plt.plot(x1,y1, label='Frequency of top 20 ngrams')
#plt.xlabel('x1')
#plt.ylabel('y1')
#plt.title('Frequency of top 20 ngrams')
#plt.legend()
#plt.show() 
##
##         
##
##


plt.plot(x_smooth,bspl_y, label='-1,-2,-2 ngram')
plt.plot(x_smooth1,bspl_y1, label='-1,-2,2 ngram')
plt.plot(x_smooth2,bspl_y2, label='-1,-2,0 ngram')
plt.xlabel('year')
plt.ylabel('frequency')
plt.title('Top 3 ngrams')
plt.legend()
plt.show()

plt.plot(fx,fy, label='-1,-2,-2 ngram')
plt.plot(fx1,fy1, label='-1,-2,2 ngram')
plt.plot(fx2,fy2, label='-1,-2,0 ngram')
plt.xlabel('year')
plt.ylabel('frequency')
plt.title('Top 3 ngrams without smoothing')
plt.legend()
plt.show()

