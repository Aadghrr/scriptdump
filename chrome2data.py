#Func for converting request data copied in chrome into a dict

def c2d(s):
    return {x.split(': ')[0]:x.split(': ')[1] for x in s.split('\n') if x!=''}
