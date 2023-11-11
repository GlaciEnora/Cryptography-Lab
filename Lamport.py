#Hashing Lamport
#Inputs: prime, root

def Lamport(p, r, x):
    k = len(x)
    y = [[None for i in range(2)] for i in range(k)]

    for i in range(k):
        for j in range(2):
            y[i][j] = int(input("Enter the random hash number: "))
    print(y)

    def f(p, r, i):
        return (r**i)%p

    z = []
    for i in range(k):
        z_row = []
        for j in range(2):
            z_row.append(f(p, r, y[i][j]))
        z.append(z_row)
    print(z)

    sign = [y[i][j] for i,j in zip(range(3), (x[k] for k in range(3)))]
    print("Signature: ", sign)
    print("Verification: ")
    ver = [f(p, r, sign[i]) for i in range(3)]
    print(ver)
    for i, j in zip(ver, (z[i][j] for i,j in zip(range(3), (x[k] for k in range(3))))):
        if i != j:
            print("Error")
            break
    else:
        print("Verified.")

arg = eval(input("Enter three element tuple of prime, root of prime and the messgae to be signed: "))
Lamport(arg[0], arg[1], arg[2])