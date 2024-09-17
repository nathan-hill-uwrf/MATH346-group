
# Set tolerance
tol = 1*10**-5
# Set the max number of iterations I will allow
max_runs = 100

# Set the function we are looking for roots in
def f(x):
    return 230*x**4 + 18*x**3 + 9*x**2 - 221*x

# Find the dirivative of f(x)
def fprime(x):
    return 920*x**3 + 54*x**2 + 18*x - 221

# Fucntion to find newton roots, give it a starting guess
def newton(init):
    p = init
    for x in range(max_runs):
        print('this is iteration', x)
        # The Newton method formula
        pk = p - (f(p) / fprime(p))
        # Check if we are below the tolerance
        if (abs(pk-p) < tol):
            return pk
        p = pk

    # Stop if max runs hit and still not below tolerance
    return print('max runs hit and above tolerance')

# Find roots at two diffrent starting points
root1 = newton(.5)
root2 = newton(2)

print("root found at:", root1)
print('root fount at:', root2)
