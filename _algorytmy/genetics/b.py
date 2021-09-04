s = '123456789'

def split3(s):
    return [''.join([s[i],s[i+1],s[i+2]]) for i in range(0,len(s), 3)]


print(split3(s))