def pc(x,i=0):
    if type(x)==type(dict()) and len(x)!=0:
        for k in x:
            print(' '*i,'-'*i,k,sep='')
            pc(x[k],i+1)
