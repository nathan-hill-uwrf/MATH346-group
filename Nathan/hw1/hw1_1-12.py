



import sympy as sp

x = sp.symbols('x')
f = 2*x*sp.cos(2*x)-(x-2)**2
derv = sp.diff(f,x)
derv2 = sp.diff(f,x,2)
derv3 = sp.diff(f,x,3)
derv4 = sp.diff(f,x,4)
print(derv4)
error = ((32*x)+64/sp.factorial(4))*x**4
print(error.subs(x,.4))

p3 = -4 + 6*x + -x**2 + -4*x**4
print(p3.subs(x,.4))
print(f.subs(x,.4))
print(p3.subs(x,.4) - f.subs(x,.4))
                   
