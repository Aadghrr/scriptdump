#!/usr/bin/python3
#import hexdump as h
import sys,codecs

file_signatures = { 
    b'2321' : 'Shebang script',
    b'53514c69746520666f726d6174203300' : 'sqlite db',
    b'425a68' : 'bz2 compressed',
    b'474946383761' : 'gif',
    b'474946383961' : 'gif',
    b'ffd8ffdb' : 'jpg',
    b'ffd8ffe000104a4649460001' : 'jpg',
    b'ffd8ffee' : 'jpg',
    b'ffd8ffe1????457869660000' : 'jpg',
    b'89504e470d0a1a0a' : 'png',
    b'504b0304' : 'zip and related',
    b'504b0506' : 'zip and related',
    b'504b0708' : 'zip and related',
    b'255044462d' : 'pdf',
    b'000000206674797069736f6d' : 'mp4'
    }

sigs = list(file_signatures.keys())
inputFile = sys.argv[1] 
with open(inputFile, 'rb') as f:
    for chunk in iter(lambda: f.read(32), b''):
        r = [x in codecs.encode(chunk, 'hex') for x in sigs]
        if any(r):
            k = [sigs[x] for x in range(len(r)) if r[x]][0]
            print('FOUND', file_signatures[k],k)
        if '-a' in sys.argv:
            print(codecs.encode(chunk, 'hex'))
