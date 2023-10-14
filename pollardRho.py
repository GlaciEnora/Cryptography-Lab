def func(x, c=1):
    return (x**2)+c

def gcd(a, b):
    flag = False
    for i in range(2, max(a,b)):
        if a%i == 0 and b%i == 0:
            flag = True
            return i
    if (not flag):
        return 1
    
def pollardRho(n):
    d = 1
    x = 2
    y = x
    while (d == 1) or (d == n):
        x = func(x) % n
        y = func(y) % n 
        y = func(y) % n
        d = gcd(abs(x - y), n)
        if (1 < d) and (d < n):
            return d
        
n = int(input("Enter the number to factorise: "))
print("Factors of ", n, "are ", pollardRho(n), n//pollardRho(n))