import sys, requests, json
from multiprocessing import Process

def checkCloud(ip,cloud,ipJSON,ipprefix):
    r = requests.get(ipJSON)
    r = json.loads(r.content)
    for block in r['prefixes']:
        if 'ipv6Prefix' in block.keys():
            continue
        if inCIDR(ip=ip, cidr=block[ipprefix]):
            print(ip,'owned by',cloud,' Details:',block)
            return

def checkAWS(ip):
    return checkCloud(ip,cloud='AWS',ipJSON='https://ip-ranges.amazonaws.com/ip-ranges.json',ipprefix='ip_prefix')

def checkGCP(ip):
    return checkCloud(ip,cloud='GCP',ipJSON='https://www.gstatic.com/ipranges/cloud.json',ipprefix='ipv4Prefix')

def checkAzure(ip):
    r = requests.get('https://download.microsoft.com/download/7/1/D/71D86715-5596-4529-9B13-DA13A5DE5B63/ServiceTags_Public_20200921.json')
    if 404 == r.status_code:
        return
    r = json.loads(r.content)
    for value in r['values']:
        for block in value['properties']['addressPrefixes']:
            if ':' in block:
                continue
            else:
                if inCIDR(ip=ip,cidr=block):
                    print(ip,'owned by Microsoft. Details:',block)
                    return

def inCIDR(ip=None,cidr=None):
    if None == ip:
        ip = sys.argv[1]
    if None == cidr:
        cidr = sys.argv[2]
    block = int(cidr.split('/')[-1])
    cidr = cidr.split('/')[0]
    mask = lambda y: ''.join([format(int(x),'08b') for x in y.split('.')])[:block]
    r = mask(ip) == mask(cidr)
    return r

if __name__=='__main__':
    if sys.argv.__len__() == 2:
        ip = sys.argv[1]
        procs = [Process(target=x,args=[ip]) for x in [checkAWS, checkGCP, checkAzure]]
        for proc in procs:
             proc.start()
    elif sys.argv.__len__() == 3:
        ip = sys.argv[1]
        cidr = sys.argv[2]
        print(inCIDR(ip=ip,cidr=cidr))
    elif sys.argv.__len__() > 3 or not '/' in sys.argv[-1]:
        for i in sys.argv[1:]:
            ip = i
            procs = [Process(target=x,args=[ip]) for x in [checkAWS, checkGCP, checkAzure]]
            for proc in procs:
             proc.start()
    else:
        print("Usage: \n To check if IP is in range, use something like $python3 inCIDR <ip> <cidr block>\neg python3 inCIDR 192.168.0.1 192.168.0.0/21 \n To check if IP belongs to a known hosting service use inCIDR <ip> ")
    
