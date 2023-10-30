#Pollard Rho discrete logarithm version

def modinv(num, mod):
    if num == 1:
        return 1
    if num > mod:
        return modinv(num%mod, mod)
    else:
        for i in range(2, mod):
            if (num*i)%mod == 1:
                return i
            
def s1(x, a, b, n, alp = 0, bet = 0):
    return ((bet*x)%n, a%n, (b+1)%n)

def s2(x, a, b, n, alp = 0, bet = 0):
    return ((x**2)%n, 2*a %n, 2*b %n)

def s3(x, a, b, n, alp=0, bet=0):
    return((alp*x)%n, (a+1)%n, b%n)

def loop(x, a, b, i, aleph, beth, n):
    lkp1 = []
    lkp2 = []
    while  (True):
        i+=1
        if x%3 == 1:
            lkp1.append(s1(x, a, b, n, aleph, beth))
            x = (beth*x)%n
            b = b+1 % n
            if i%2 == 0:
                lkp2.append((x, a, b))
#                print("L2: ", lkp2[-1])
        elif x%3 == 0:
            lkp1.append(s2(x, a, b, n, aleph, beth))
            x = (x**2)%n
            a = 2*a % n
            b = 2*b % n
            if i%2 == 0:
                lkp2.append((x, a, b))
#                print("L2: ", lkp2[-1])
        else:
            lkp1.append(s3(x, a, b, n, aleph, beth))
            x = (aleph*x)%n
            a = a+1 % n
            if i%2 == 0:
                lkp2.append((x, a, b))
#                print("L2: ", lkp2[-1])
#        print("L1: ", lkp1[-1])
        if (lkp2 != [] and lkp2[-1][0] == lkp1[len(lkp2)-1][0]):
            return (lkp1[len(lkp2)-1][1], lkp1[len(lkp2)-1][2], lkp2[-1][1], lkp2[-1][2])

def rho(aleph, beth, p, n):
    x, a, b = 1, 0, 0
    arg = loop(x, a, b, 0, aleph, beth, p)
    c = ((arg[0]-arg[2])*modinv(arg[3]-arg[1], n))%n
    print(c)
    print("Proof: ")
    print("LHS: ", aleph**c % p)
    print("RHS: ", beth)


alp = int(input("Enter alpha: "))
bet = int(input("Enter beta: "))
prime = int(input("Enter prime: "))
n = int(input("Enter the order: "))
rho(alp, bet, prime, n)
