import random

def getperm(l):
    seed = sum(l)
    random.seed(seed)
    perm = list(range(len(l)))
    random.shuffle(perm)
    random.seed()
    return perm


def permute(l):
    perm = getperm(l)
    l[:] = [l[j] for j in perm]


def unshuffle(l):
    perm = getperm(l)
    res = [None] * len(l)
    for i, j in enumerate(perm):
        res[j] = l[i]
    l[:] = res
    
def numer(lis):
    sub = []
    for i in lis:
        sub.append(int(i, 2))
    return sub

def desubstitute(lis):
    bus = []
    sbox = [3, 10, 14, 11, 15, 4, 5, 12, 13, 0, 1, 2, 7, 9, 8, 6]
    for i in lis:
        bus.append(sbox[i])
    return bus

def substitute(lis):
    sub = []
    sbox = [9, 10, 11, 0, 5, 6, 15, 12, 14, 13, 1, 3, 7, 8, 2, 4]
    for i in lis:        
        sub.append(sbox[i])
    return sub

def xor(a, b):
    x = list( i ^ j for i, j in zip(a, b))
    return x

pt = input("Enter the binary string separated by '/': ")
pt_lis = pt.split('/')
key = input("Enter the binary key separated by '/': ")
key_lis = key.split('/')
print(pt_lis)
print(key_lis)
subkey = []
for i in range(len(pt_lis)+1):
    subkey.append(numer(key_lis[i:i+4]))
#print(subkey)
w = numer(pt_lis)
#print(w)

for i in range(len(pt_lis)):
    u = xor(w, subkey[i])
    print(u)
    v = substitute(u)
    print(v)
    permute(v)
    w = v
    print(w)
W = xor(w, subkey[len(pt_lis)])
print("End of encryption: ", W)

for i in range(len(pt_lis)):
    u = xor(W, subkey[-(i+1)])
    print(u)
    unshuffle(u)
    v = u
    print(v)
    W = desubstitute(v)
    print(W)
w = xor(W, subkey[0])
ct_lis = []
for i in w:
    ct_lis.append(str(bin(i)).replace('0b', ''))
print(ct_lis)
ct = '/'.join(ct_lis)
print("End of decryption: ", ct)


