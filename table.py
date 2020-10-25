import statistics as stat
from collections import defaultdict

def group(corpus):
    dd={j:sum([j == i for i in a]) for j in set(corpus)}
    return {i[0]:i[1] for i in sorted(dd.items(),key=lambda x:x[1],reverse=True)}

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

def chooseDelim(delims,allDelims):
    dd = defaultdict(int)
    dd.update(allDelims)
    return sorted(delims,key=lambda x:dd[x], reverse=True)[0]    

def chooseRowDelim(rowDelims):
    return chooseDelim(rowDelims,{'\n':1})

def chooseColDelim(colDelims):
    return chooseDelim(colDelims,{',':1,'\t':2})

def findDelims(corpus, approxRows=500, approxCols=6, minSD=15):
    characters = group(corpus)
    dic = {character:stat.stdev(diff(findall(corpus,character))) for character in characters if characters[character]>approxRows}
    dic = {x[0]:x[1] for x in sorted(dic.items(),key=lambda x:x[1])}
    delims = [(i,characters[i]) for i in dic if dic[i]<minSD]
    colDelims = [d[0] for d in delims if d[1]>approxRows*approxCols]
    rowDelims = [d[0] for d in delims if not d[0] in colDelims]
    return rowDelims, colDelims

def generatetable(corpus, approxRows=500,approxCols=6):
    rowDelims, colDelims = findDelims(corpus)
    print("Possible delimiters\nRow:",rowDelims,"\nCols:",colDelims)
    rowDelim = chooseRowDelim(rowDelims)
    colDelim = chooseColDelim(colDelims)
    print("Using",rowDelim.__repr__(),"and",colDelim.__repr__())
    table = [row.split(colDelim) for row in corpus.split(rowDelim) if len(row)>approxCols]
    return table
