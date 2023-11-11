#Oil and Vinegar atrocity
from sympy import *

a, b, c, d = symbols("a b c d")
val = (a, b, c, d)

def S(a, b, c, d, inv=0):
    if inv == 0:
        return (b+d+1, a+d+1, b+c+d, a+b+c+d)
    else:
        return ((c+d)%2, (a+b+c+d)%2, (a+c+1)%2, (b+c+d+1)%2)

def f1(x):
    expr = a*b + b*c + d
    return expr.subs({a:x[0], b:x[1], c:x[2], d:x[3]}, simultaneous = True)

def f2(x):
    expr = a*c + b*d + b
    return expr.subs({a:x[0], b:x[1], c:x[2], d:x[3]}, simultaneous = True)

def Oil_Vin(x, y):
    #According to our example, x = 0, y = 1
    #Calculation of f1pub and f2pub
    #By definitions, fnpub = fn(S(val))
    f1pub = f1pub = Poly(expand(f1(S(a, b, c, d))), modulus = 2)
    print(f1pub.as_expr())

    f2pub = Poly(expand(f2(S(a, b, c, d))), modulus = 2)

    #Issues to be known: Getting an additional a**2 + b**2 in f2pub. A proposed solution is as follows.
    '''This part is kind of hard to understand, but basically, I am adding a template polynomial that contains the terms we want to remove, under O(). Then using the removeO method of the expr class, I am removing all terms that are similar to the ones in O(). This removes the a**2 + b**2'''

    f2pub = f2pub.add(Poly(O(a**2+b**2+c**2+d**2)))
    f2pub = Poly(f2pub).as_expr().removeO()
    print(f2pub)

    #Here I substitute the vinegar variables, which we took as input. 
    f1pub = Poly(f1pub.subs({a:x, b:y}), modulus = 2).as_expr()
    f2pub = f2pub.subs({a:x, b:y}, simultaneous = True)
    #f2pub does not need the Poly class as we've already converted it to an expr form while removing O()
    #We use as_expr here to solve the system of equations
    #The following returns the remaining two variables
    res = solve([f1pub-x, f2pub-y], c, d, dict=True)
    print(res)

    #The following is the signing process
    '''Signing process:
        Given a 2n tuple (a, b, c, d), the signing is done by 
        performing S^-1(a, b, c, d)'''
    sign = S(x, y, res[0][c], res[0][d], inv=-1)

    #The following is the verification process
    F1 = expand(f1(S(a, b, c, d))).subs({i:j for i, j in zip(val, sign)}, simultaneous = True)%2
    F2 = expand(f2(S(a, b, c, d))).subs({i:j for i, j in zip(val, sign)}, simultaneous = True)%2

    print("Signing: ", sign)
    print("Verification: ")
    print("f1pub(sign): ", F1)
    print("f2pub(sign): ", F2)
    if ((F1, F2)==(x,y)):
        print("Hence Verified.")
    else:
        print("Error in the algorithm. Please reverify")

#Main
tup = eval(input("Enter the tuple to be used under the signing scheme: "))
Oil_Vin(tup[0], tup[1])