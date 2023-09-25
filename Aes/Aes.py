import random

def shift(mat):
    for i in range(4):
        mat[i] = mat[i][i:] + mat[i][:i]

def revshift(mat):
    for i in range(4):
        mat[i] = mat[i][-i:] + mat[i][:-i]

def xor(mat, key):
    temp = [[] for i in range(4)]
    for i in range(4):
        for j in range(4):
            temp[i].append(str(hex(int(mat[i][j], 16) ^ int(key[i][j], 16))).replace("0x", ""))
            if len(temp[i][j]) == 1: temp[i][j] = "0" + temp[i][j]
    return temp

pt = input("Enter a 16 letter word: ")
mat = [["0" for i in range(4)] for i in range(4)]
cp = 0
for i in range(4):
    for j in range(4):
        mat[i][j] = str(hex(ord(pt[cp]))).replace("0x", "")
        cp += 1
print("Plaintext: ", mat)
sub = [["0" for i in range(4)] for i in range(4)]
for i in range(4):
        for j in range(4):
            sub[i][j] = str(hex(random.randrange(256))).replace("0x", "")
            if len(sub[i][j]) == 1: sub[i][j] = "0" + sub[i][j]
print("Key: ", sub)
mat2 = xor(mat, sub)
shift(mat2)
print("Encryption: ", mat2)
revshift(mat2)
mat1 = xor(mat2, sub)
print("Decryption: ", mat1)




