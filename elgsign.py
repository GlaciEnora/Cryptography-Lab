def modinv(a, mod):
    if (a > mod):
        return modinv(a%mod, mod)
    else:
        for i in range(2, mod):
            if (a*i)%mod == 1:
                return i
        
def sign(alpha, k, p, x):
    gamma = (alpha**k) % p
    delta = ((x - (a*gamma))*modinv(k, p-1))%(p-1)

    return (gamma, delta)

def verify(alp, a, p, x):
    bet = (alp**a) % p
    k = int(input("Enter a random integer: "))
    gam, delt = sign(alp, k, p, x)
    lhs = ((bet**gam)*(gam**delt))%p
    rhs = (alp**x)%p
    if lhs == rhs:
        print("The given signature scheme is valid.")
    else:
        print("An error has occured. Please reverify")

p = int(input("Enter your modular prime: "))
alpha = int(input("Enter the primitive root of the given prime: "))
a = int(input("Enter a random integer: "))
x = int(input("Enter your base plaintext: "))
verify(alpha, a, p, x)