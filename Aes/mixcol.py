#MixColumns module

def Xor(arg):
    x = 0
    for i in arg:
        x ^= i
    return x

def galoismul(a, b):
    p = 0
    for i in range(8):
        if a == 0 or b == 0:
            break

        if b & 0x01:
            p ^= a

        b >>= 1
        carry = a & 0x80
        a <<= 1
        if carry:
            a ^= 0x11b    
    return p

def shift_l(lis):
    lis = lis[-1:]+lis[:-1]
    return lis

def mixcol(mat):
    cons_mat = []
    cons = [0x02, 0x03, 0x01, 0x01]
    for i in range(4):
        cons_mat.append(cons)
        cons = shift_l(cons)
    print(cons_mat)
    res = []
    for i in range(4):
        raw=[]
        for j in range(4):
            prod = 0
            for k in range(4):
                #print(mat[i][k], cons[k][j])
                prod ^= galoismul(cons_mat[i][k], mat[k][j])
            raw.append(prod)
        res.append(raw)

    return res
