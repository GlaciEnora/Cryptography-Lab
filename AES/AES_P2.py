k=[[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]

def xor(a,b):
    s=""
    for i,j in zip(a,b):
        if i==j:
            s+="0"
        else:
            s+="1"
    return (s)

def bin(b):
    l=list("0123456789ABCDEF")
    x=""
    for i in b:
        a=l.index(i)
        b=""
        while a>0:
            b=str(a%2)+b
            a=a//2
        while len(b)<4:
            b="0"+b
        x+=b
    return x
def deci(a):
    f=0
    for i in range(len(a)):
        if a[i]=='1':
            f+=(2**(len(a)-1-i))

    return f
def d1(a):
    v=a[:4]
    v=deci(v)
    u=a[4:]
    u=deci(u)
    l=list("0123456789ABCDEF")
    x=""
    x=l[v]+l[u]
    return (x)

def s2(a):
    b=a
    if b[0]=="1":
        b=b[1:]+"0"
        b=xor(b,bin("1B"))
    else:
        b=b[1:]+"0"
    return b

def s3(a):
    b=s2(a)
    return xor(b,a)

def MC(a,b):
    c=[]
    p,q,r=("00000000","00000000","00000000")
    for i in range(0,len(b[0])):
        c.append([])
        for j in range(0,len(a)):
            s="00000000"
            for k in range(0,len(b)):
                if a[j][k]==1:
                    p=bin(b[k][i])
                    s=xor(s,p)
                if a[j][k]==2:
                    q=s2(bin(b[k][i]))
                    s=xor(s,q)
                if a[j][k]==3:
                    r=s3(bin(b[k][i]))
                    s=xor(s,r)
            c[i].append(d1(s))
    return c


