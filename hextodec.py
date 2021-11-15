#!/usr/bin/python3
import sys
h = sys.argv[1]
d = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
h.lower()
h = list(h)
h.reverse()
try:
    r=0
    for i in range(len(h)):
        r=r+d[h[i]]*(16**i)
    print(r)
except KeyError:
    print('Error - not a valid hex number')
