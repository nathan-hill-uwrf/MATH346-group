# Set your function (give in g(x) form)
g = "(3*x**4+2*x**2+3)/(4*x**3+4*x-1)"

# Set a tolerance
tol = 1*10**-6


# Call this to compute g(x) at given x
def fun(x):
    return eval(g)

# When you call the fixed point iteration function give it a starting x
def fpi(x0):
    next_x = fun(x0)
    lst_x = x0
    # Check if starting value is already a fixed point
    if(abs(next_x - x0) < tol):
        return print("Given start value is a fixed point.")
    # Loop to find fixed point
    while (abs(next_x - lst_x) > tol):
        # Save the current x value as last x
        lst_x = next_x
        # Compute the next x value and store it
        next_x = fun(next_x)

    print("fixed point at: ", next_x)
    # Somewhat redundant second print statement.
    # fun(next_x) should equal next_x within the tolerance.
    # I like to show that the fpi function is working.
    print("g(x) at fixed point is: ", fun(next_x))


# Different input values
fpi(0)
fpi(1)
# Test to ensure if statement above works
fpi(-0.8760531158)
