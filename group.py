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

def findDelims(corpus, approxRows=500, approxCols=6, minSD=15):
    import statistics as stat
    characters = group(corpus)
    dic = {character[0]:stat.stdev(diff(findall(corpus,character[0]))) for character in characters if character[1]>approxRows}
    dic = sorted(dic.items(),key=lambda x:x[1])
    delims = [(i[0],characters[i[0]]) for i in dic if i[1]<minSD]
    rowDelims = [d[0] for d in delims if d[1]>approxRows*approxCols]
    colDelims = [d[0] for d in delims if not d[0] in rowDelims]
    return rowDelims, colDelims

if __name__ == '__main__':
    rowDelim, colDelim = findDelims(corpus)
    table = [row.split(rowDelim) for row in corpus.split(colDelim)]
    for row in table[:25]:
        print(row)
    print('...')
