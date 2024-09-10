

import math

# Set your function
f = "math.sin(x) + .7"


# Set a tolerance
tol = 1*(10**-4)

# Call this to fill in value for x
def fun(x):
    return eval(f)

# Set your a and b when you call bisec
def bisec(a,b):
# Check the signs on a and b put the possitive value in a and vice versa
    if (fun(a)>0 and fun(b)>0):
        print('both values same sign')
        return 0
    elif (fun(b)>0):
        swap_store = a
        a = b
        b = swap_store
    elif (fun(a)<tol or fun(b)<tol):
        print('root already on interval maxima')
    c = (a+b)/2
    while (abs(fun(c)) > tol):
        print(a)
        print(b)
        c = (a+b)/2
        if (fun(c)>0):
            a = c
        else:
            b = c
        print(fun(c))

    print('root of f(x): ', c)
    print(fun(c))


bisec(-2,0)
