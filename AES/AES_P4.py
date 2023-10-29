def shift(a,i):
    while i>0:
        a.append(a[0])
        a=a[1:]
        i-=1
    return a
def shiftrows(c):
    for i in range(0,4):
        c[i]=shift(c[i],i)
    return c

def addroundkey(a, b):
    c=[]
    l=list("0123456789ABCDEF")
    for i in range(0,4):
        c.append([])
        for j in range(0,4):
            v=int(a[i][j], 16) ^ int(b[i][j], 16)
            c0 = hex(v).replace("0x", "")
            if len(c0) == 1: c0 = "0" + c0
            c[i].append(c0)
    return c
