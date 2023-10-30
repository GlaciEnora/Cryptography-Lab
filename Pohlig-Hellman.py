#DISCRETE LOGARITHM ALGORITHMS
#Credits to Sai Harini
#POHLIG-HELLMAN
import math
def prime_factor(n):
    l=[]
    while n%2==0:
        l.append(2)
        n=n//2
    for i in range(3,n+1,2):
        while n%i==0:
            l.append(i)
            n=n//i
    d={}
    for i in l:
        if i not in d.keys():
            d[i]=1
        else:
            d[i]+=1
    return d

def pohlig_hellman(p,al,b):
    alist={}
    n=p-1
    d=prime_factor(n)
    l=[]
    a=0
    ini_b=b
    crt={}
    for i in d.keys():
        l.append(i)
    print(l)
    for i in l:
        tlist=[]
        q=i
        print("q : ",q)
        c=d[i]
        print("C : ",c)
        j=0
        b=ini_b
        while(j<=(c-1)):
            de=(b**(n/(q**(j+1))))
            de=de%p
            print("delta : ",de)
            for k in range(n):
                if(((al**((k*n)/q))%p)==de):
                    print(k)
                    a=k
                    tlist.append(a)
                    break
            t=a*(q**j)
            b=b*(1/(al**t))
            j=j+1
        alist[i]=tlist
        sum=0
        for i in range(c):
            sum+=(tlist[0]*(q**i))
        crt[q*c]=sum
    return alist,crt

def inv(a,b):
    r=1
    t1=0
    t2=1
    while(r!=0):
        q=a//b
        r=a%b
        t=t1-(q*t2)
        a=b
        b=r
        t1=t2
        t2=t
    return t1

def CRT(d,p):
    m=1
    mod=[]
    mval=[]
    minv=[]
    xval=0
    for i in d.keys():
        m=m*i
    for i in d.keys():
        mod.append(i)
    for i in d.keys():
        mval.append(m//i)
    for i in range(len(mval)):
        x=inv(mod[i],mval[i])
        while(x<0):
            x=x+mod[i]
        minv.append(x)
    for i in range(len(mod)):
        xval+=mval[i]*d[mod[i]]*minv[i]
    xval=xval%(p-1)
    print(xval)
    
            
p=int(input('enter p val : '))
al=int(input('enter alpha value : '))
beta=int(input('enter beta value : '))
x,y=pohlig_hellman(p,al,beta)
print(x)
print(y)
CRT(y,p)
