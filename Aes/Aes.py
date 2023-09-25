import random

def shift(mat):
    for i in range(4):
        mat[i] = mat[i][i:] + mat[i][:i]

def revshift(mat):
    for i in range(4):
        mat[i] = mat[i][-i:] + mat[i][:-i]

pt = input("Enter a 16 letter word: ")
mat = [["0" for i in range(4)] for i in range(4)]
cp = 0
for i in range(4):
    for j in range(4):
        mat[i][j] = ord(pt[cp])
        cp += 1
print("Plaintext: ", mat)
