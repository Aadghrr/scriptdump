import hashlib
from string import ascii_letters

uppers = ascii_letters.upper()[:26]
nums = ''.join([str(x) for x in range(10)])
hexChar = nums+'ABCDEF'

h = input('Enter suspected hash:').upper()
if len(h)!=32:
  raise(Exception('Not a 32 char hex string'))
if not all([x in hexChar for x in h]):
  raise(Exception('Not a hex string'))

salts = input('Enter comma separated list of possible salts:').split(',')
r = int(input('Enter possible range upper limit int: '))

def iterator(h,salt,rng,enc='UTF-8'):
    found = 0
    for i in range(rng):
        temp = hashlib.md5(bytes(salt,enc)+bytes(i)).hexdigest().upper()
        #print(temp,'\t',h)
        if temp == h:
            print('-- Match found --','\n','md5:',salt,enc,i)
            found = 1
            break
    if found == 0:
        print('Nothing found, try increasing the range or  number of salts')

saltList = salts + ['/'.join(salts)] + ['.'.join(salts)] +['']

for salt in saltList:
    iterator(h,salt,r)
