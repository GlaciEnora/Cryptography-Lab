def modinverse(num1, num2):
    for i in range(2, num2):
        if (num1*i) % num2 == 1:
            return i
        else:
            pass
        
def add_inv(pt, mod):
    return (pt[0], (-pt[1])%mod)

def validate(p1, a, b):
    expr = p1[1]**2 - ((p1[0]**3) + (a * p1[0]) + b)
    if expr == 0:
        return True
    else:
        return False
    
def pointmul(mod, a, p1, n):
    safe = p1
    num = list(bin(n).replace("0b", "")[::-1])
    print(num)
    pow = 1
    for i in num[1:]:
        if i == '1':
            temp = pow
            while(temp != 0):
                p1 = point_add(mod, a, p1)
                temp -= 1
        else:
            pass
        pow += 1
    if num[0] == '1':
        p1 = point_add(mod, a, p1, safe)
    return p1

def point_add(mod, a, p1, p2 = (0, 0)):
    if p2 != (0,0):
        lam = ((p2[1] - p1[1])*modinverse(p2[0]-p1[0], mod)) % mod
        x = (lam**2 - p1[0] - p2[0]) % mod
        y = (lam*(p1[0] - x) - p1[1]) % mod
        return (x, y)
    elif p1 == p2 or p2 == (0,0):
        lam = (((3 * (p1[0]**2)) + a) * modinverse(2*p1[1], mod)) % mod
        x = (lam**2 - (2*p1[0])) % mod
        y = (lam*(p1[0] - x) - p1[1]) % mod
        return (x,y)

print(pointmul(67, 2, (2, 22), 5))
a = int(input("Enter the a coefficient: "))
b = int(input("Enter the b coefficient: "))
mod = int(input("Enter the mod: "))
print("Given curve is: y^2 = x^3 +", a, "x + ", b)
d = int(input("Enter a random integer: "))
e1 = eval(input("Enter the first point: "))
pt = eval(input("Enter the plaintext point: "))
if validate(e1, a, b) and validate(pt, a, b):
    print("Valid point.")
else:
    print("Invalid point.")
print("Encryption. . . ")
e2 = pointmul(mod, a, e1, d)
c1 = pointmul(mod, a, e1, 2)
samp = pointmul(mod, a, e2, 2)
c2 = point_add(mod, a, pt, samp)
print("Cipher text: ", c1, c2)
print("Decryption . . . ")
p1 = pointmul(mod, a, c1, d)
p1 = add_inv(p1, mod)
pt = point_add(mod, a, c2, p1)
print("Plain text: ", pt)