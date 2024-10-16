import numpy

def f(x):
    return x**5 - 15*x**4 + 85*x**3 - 225*x**2 + 274*x - 120

tol = 10**-6

# give this function init three points
def muller_book(p,p1,p2):
    # construct a porabola using these points
    h1= p1 - p
    h2= p2 - p1
    fp1 = f(p1)
    fp2 = f(p2)
    ## find slopes from point to point
    slope1 = (fp1 - f(p))/h1
    slope2 = (fp2 - fp1)/h2
    ## start setting up the quadradic formula
    d = (slope2 - slope1)/(h1+h2)
    b = slope2 + h2*d
    complex_check = b**2 - 4*fp2*d
 #   if complex_check < 0:
 #       return print("complex root")
    sqrroot = numpy.emath.sqrt(complex_check)
    if abs(b - sqrroot) < abs(b + sqrroot):
        e = b + sqrroot
    else:
        e = b - sqrroot
    quadradic = -2*fp2/e
    p3 = p2 + quadradic
    if f(p3) < tol:
        return print(p3)
    return muller_book(p1,p2,p3)

# def muller_lin(p,p1,p2):
#     sol = [[f(p)],
#            [f(p1)],
#            [f(p2)]]
#     equ = [[p**2, p, 1],
#            [p1**2, p1, 1],
#            [p2**2, p2, 1]]
#     a,b,c = numpy.linalg.solve(equ,sol)
#     a,b,c = a[0],b[0],c[0]
    
#     rootofpoints = p2
#     if b > 0:
#         rootofpoints = (b + numpy.sqrt(b**2 - 4*a*c))/2*a
#     else:
#         rootofpoints = (b - numpy.sqrt(b**2 - 4*a*c))/2*a

#     if abs(f(rootofpoints)) < tol:
#         return print("root at:", rootofpoints, "\n",
#                      "value = ", f(rootofpoints))
#     else:
#         return muller_lin(p1,p2,rootofpoints)
        
    
           

muller_book(-10,2,3)
muller_book(0,5,10)
#muller_lin(-10,2,3)
