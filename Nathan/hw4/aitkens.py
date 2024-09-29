

def f(x):
    return x**5 + -15*x**4 + 85*x**3 + -225*x**2 + 274*x + -120

def g(x):
    return (x**5 + -15*x**4 + 85*x**3 -225*x**2 -120)/-274

tol = 10**-7

def fpi(x_init):
    print("-------", "Given start point:", x_init, "-------")
    # Set Pn through Pn+2
    Pn = x_init
    Pn1 = g(x_init)
    Pn2 = g(Pn1)

    # Check if starting value is already a fixed point
    if(abs(Pn1 - Pn) < tol):
        return print("Given start value:", x_init, " is a fixed point.")
        
    # Set first Phat
    # The Phat equation is Pn - (delta(Pn))^2/delta^2(Pn)
    Phat = Pn - ((Pn1-Pn)**2 / (Pn2 - 2*Pn1 + Pn))
    iteration_count = 1
    # Loop to find fixed point
    while (abs(Phat-g(Phat)) > tol):
        Pn = Pn1
        Pn1 = Pn2
        Pn2 = g(Pn2)
        Phat = Pn - ((Pn1-Pn)**2 / (Pn2 - 2*Pn1 + Pn))
        iteration_count += 1

    # Print out info
    print("Values of intrest")
    print("Pn:", Pn)
    print("Pn+1:", Pn1)
    print("Pn+2:", Pn2)
    print("Phat (fixed point):", Phat)
    print("iteration count:", iteration_count)

fpi(0)
fpi(1.5)
fpi(2.01)
fpi(3.8)
fpi(4.5)
fpi(7)
fpi(4)
fpi(2)
