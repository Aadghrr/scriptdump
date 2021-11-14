def flatten(arg):
    res = []
    def flat(arg):
        if hasattr(arg,'__iter__') and (type(arg)!=type(str()) or len(arg)>1 ):
            for i in arg:
                flat(i)
        else:
            res.append(arg)
    flat(arg)
    return res
