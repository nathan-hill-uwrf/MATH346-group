import math

# Set your function
f = "math.sqrt(x) - math.cos(x)"


# Set a tolerance
tol = 1*(10**-6)

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
    psubx = 1
    while (abs(fun(c)) > tol):
        c = (a+b)/2
        psubx += 1
        if (2 < psubx < 6):
            print('p' + str(psubx), ' = ', c)
        if (fun(c)>0):
            a = c
        else:
            b = c

    print('root of f(x): ', c)


bisec(0,1)
