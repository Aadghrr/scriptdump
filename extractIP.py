#!/usr/bin/python3
import re,sys

with open(sys.argv[1]) as fd:
    res = fd.read()

r = r'\t(?:[0-9]{1,3}\.){3}[0-9]{1,3}'
for i in re.findall(r,res):
    print(i[1:])
