#!/usr/bin/python3
import sys, requests, json, os, datetime
from multiprocessing import Process

def checkCloud(ip,cloud,ipJSON,ipprefix):
    name = 'ips_'+cloud+datetime.datetime.now().strftime('%Y%m%d')
    if not name in os.listdir():
        r = requests.get(ipJSON)
        r = json.loads(r.content)
        with open(name,'w') as f:
            f.write(json.dumps(r))
    else:
        r = json.loads(open(name,'r').read())
    for block in r['prefixes']:
        if 'ipv6Prefix' in block.keys():
            continue
        if inCIDR(ip=ip, cidr=block[ipprefix]):
            return {'provider':cloud,'ip':ip,'block':block}
    return None

def checkAWS(ip):
    res= checkCloud(ip,cloud='AWS',ipJSON='https://ip-ranges.amazonaws.com/ip-ranges.json',ipprefix='ip_prefix')
    return res

def checkGCP(ip):
    res= checkCloud(ip,cloud='GCP',ipJSON='https://www.gstatic.com/ipranges/cloud.json',ipprefix='ipv4Prefix')
    return res

def checkAzure(ip):
    name = 'ips_azure'+datetime.datetime.now().strftime('%Y%m%d')
    if not name in os.listdir():
        #r = requests.get('https://download.microsoft.com/download/7/1/D/71D86715-5596-4529-9B13-DA13A5DE5B63/ServiceTags_Public_20200921.json')
        a=requests.get('https://www.microsoft.com/en-us/download/confirmation.aspx?id=56519')
        ind=str(a.content).find('json')
        r = requests.get(str(a.content)[ind-111:ind+4])
        r = json.loads(r.content)
        with open(name,'w') as f:
            f.write(json.dumps(r))
    else:
        r = json.loads(open(name,'r').read())
    for value in r['values']:
        for block in value['properties']['addressPrefixes']:
            if ':' in block:
                continue
            else:
                if inCIDR(ip=ip,cidr=block):
                    res= {'provider':'Azure','ip':ip,'block':block}
                    return res
    return None

def main(ip):
    if type(ip) != list:
        ip = [ip]
    values = []
    for i in ip:
        res = [checkAzure(i),checkAWS(i),checkGCP(i)]
        for x in res:
            if x != None:
                values.append(x)
    if 0 <len(values):
        return values
    else:
        return [{'provider':'unknown', 'ip':ip,'block':'IP not found in AWS, GCP, or Azure'}]

def mainp(ip):
    for r in main(ip):
        print(str(r).split('\\n'))

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
        res = main(ip)
        print(res)
    #    procs = [Process(target=x,args=[ip]) for x in [checkAzure,checkAWS,checkGCP]]
    #    for proc in procs:
    #         proc.start()
    elif sys.argv.__len__() == 3:
        ip = sys.argv[1]
        cidr = sys.argv[2]
        print(inCIDR(ip=ip,cidr=cidr))
    elif sys.argv.__len__() > 3 or not '/' in sys.argv[-1]:
        l=sys.argv[1:]
        procs = [Process(target=mainp,args=[ips]) for ips in [l[x*len(l)//3:(1+x)*l.__len__()//3] for x in range(3)]]
        for proc in procs:
             proc.start()
    else:
        print("Usage: \n To check if IP is in range, use something like $python3 inCIDR <ip> <cidr block>\neg python3 inCIDR 192.168.0.1 192.168.0.0/21 \n To check if IP belongs to a known hosting service use inCIDR <ip> ")
