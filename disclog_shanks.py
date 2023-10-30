#Shank's discrete logarithm algorithm
import math

def modinv(num, mod):
    if num == 1:
        return 1
    if num > mod:
        return modinv(num%mod, mod)
    else:
        for i in range(2, mod):
            if (num*i)%mod == 1:
                return i
            
def shanks(aleph, beth, z):
    n = z - 1
    m = math.ceil(n**0.5)
    firstlist = []
    secondlist = []
    x, y = 0, 0
    for j in range(m):
        tup = (j, (aleph**(m*j))%z)
        firstlist.append(tup)
        firstlist.sort(key = lambda x:x[1])
        print(firstlist)
    for i in range(m):
        tup = (i, (beth*(modinv(aleph**i, z)))%z)
        secondlist.append(tup)
        secondlist.sort(key = lambda x:x[1])
        print(secondlist)
    for item1 in firstlist:
        for item2 in secondlist:
            if item1[1] == item2[1]:
                x = item1[0]
                y = item2[0]
    res = ((m*x)+y)%z
    print(res)
    print("Proof: ")
    print("LHS: ", (aleph**res)%z)
    print("RHS: ", beth)

alp = int(input("Enter the base: "))
bet = int(input("Enter the exponent: "))
z = int(input("Enter the modular value: "))
shanks(alp, bet, z)