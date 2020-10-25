def group(a):
    dd={j:sum([j == i for i in a]) for j in set(a)}
    return sorted(dd.items(),key=lambda x:x[1],reverse=True)

def findall(s,c):
    s=list(s)
    ind = True
    res = []
    while ind:
        try:
            ind = s.index(c)
            res.append(ind)
            s.pop(ind)
        except ValueError:
            ind = None
    return res

def diff(f):
    return [f[i]-f[i-1] for i in range(1,len(f))]
