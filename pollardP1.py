def gcd(a, b):
    flag = False
    for i in range(2, max(a,b)):
        if a%i == 0 and b%i == 0:
            flag = True
            return i
    if (not flag):
        return 1
    
def factor(n):
    a = 2
    i = 2
    B = n**(1/6)
    while (i < B):
        a = (a**i) % n
        d = gcd(a-1, n)
        if (1 < d < n):
            return (d, n//d)
        elif d <= 1 and i+1 >= B:
            B += 1
            pass
        i+=1

n = int(input("Enter the number to factorise: "))
print(factor(n))