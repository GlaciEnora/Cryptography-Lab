import AES_P1 as p1
import AES_P2 as p2
import AES_P3 as p3
import AES_P4 as p4
inblk="0123456789ABCDEFFEDCBA9876543210"
key="0F1571C947D9E8590CB7ADD6AF7F6798"
def transpose_3(arg):
    st = []
    for i in range(0, 11):
        final = []
        for j in range(0, 4):
            spc = []
            for k in range(0, 4):
                spc.append(arg[i][k][j])
            final.append(spc)
        st.append(final)
    return st

def transpose_2(arg):
    st = []
    for i in range(0, 4):
        spc = []
        for j in range(0, 4):
            spc.append(arg[j][i])
        st.append(spc)
    return st

def blk_to_st(b):
    st=[]
    a=[b[i:i+2] for i in range(0,len(b),2)]
    for i in range(0,4):
        temp=[]
        temp.extend([a[4*i],a[4*i+1],a[4*i+2],a[4*i+3]])
        st.append(temp)
    return st

def plainkeyblock(b):
    st=[]
    samp = []
    a=[b[i:i+2] for i in range(0,len(b),2)]
    for i in range(0,4):
        temp=[]
        temp.extend([a[4*i],a[4*i+1],a[4*i+2],a[4*i+3]])
        samp.append(temp)
    for i in range(0, 4):
        spc = []
        for j in range(0, 4):
            spc.append(samp[j][i])
        st.append(spc)

    return st

def st_to_blk(st):
    blk=""
    for i in range(0,4):
        for j in range(0,4):
            blk+=st[j][i]
    return blk
def sub_gen(st):
    sb=[]
    for i in range(0,4):
        temp=[]
        for j in range(0,4):
            a=p1.sbox(int(st[i][j],16))[2:].upper()
            if len(a)==1:
                a="0"+a
            temp.append(a)
        sb.append(temp)
    return sb
mat = p3.Key_Expansion(blk_to_st(key))
def Encrption(inblk,mat):
    l = transpose_3(mat)
    s=plainkeyblock(inblk)
    h=0
    s=p4.addroundkey(s,l[h])
    for i in range(0,10):
        h += 1
        s=sub_gen(s)
        s=p4.shiftrows(s)
        if i!=9:
            s=p2.MC(p2.k,s)
            s = transpose_2(s)
        s=p4.addroundkey(s,l[h])
    return st_to_blk(s)
print(Encrption(inblk,mat))
