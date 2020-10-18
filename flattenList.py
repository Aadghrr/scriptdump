def flatten(arg):
    res = []
    def flat(arg):
        if hasattr(arg,'__iter__'):
            for i in arg:
                flat(i)
        else:
            res.append(arg)
    flat(arg)
    return res
