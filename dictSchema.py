def pc(x,i=0):
    if type(x)==type(dict()) and len(x)!=0:
        for k in x:
            print(' '*i,'-'*i,k,sep='')
            pc(x[k],i+1)
    elif type(x)==type(list()) and len(x)>0:
        if type(x[0])==type(dict()) and len(x[0])!=0:
            print(' '*i,'L')
            self.schema(x[0],i)
