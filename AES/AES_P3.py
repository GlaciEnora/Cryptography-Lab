#Aes Key genration
import AES_P1 as p1
w=[]
rcon=["01000000","02000000","04000000","08000000","10000000","20000000","40000000","80000000","1B000000","36000000"]
def Rot_word(w):
    x=""
    for i in range(2,8):
        x+=w[i]
    x+=w[0:2]
    return x
def Sub_word(w):
    sw=""
    for i in range(0,len(w),2):
        sw+=p1.sbox(int(w[i:i+2],16))[2:].upper().zfill(2)
    return sw
def Key_Expansion(key):
    w=[]
    for i in range(0,4):
        x=""
        for j in range(0,4):
            x+=key[i][j]
        w.append(x)
    for i in range(4,44):
        if(i%4!=0):
            w.append(format(int(w[i-1],16)^int(w[i-4],16),"0X").zfill(8))
        else:
            t1=int(Sub_word(Rot_word(w[i-1])),16)^int(rcon[(i//4)-1],16)
            temp=format(int(w[i-4],16)^t1,"0X")
            w.append(temp)
    l=[]
    j=0
    c=0
    l.append([])
    for i in range(len(w)):
        l[j].append([w[i][0:2],w[i][2:4],w[i][4:6],w[i][6:]])
        c+=1
        if c%4==0 and i+1!=len(w):
            j+=1
            l.append([])
    return l
