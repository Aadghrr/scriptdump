#!/usr/bin/python3
import re,sys
res = ' '.join(sys.argv[1:])
r = r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}'
for i in re.findall(r,res):
    print(i)
