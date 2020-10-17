print("Let the equation be of form ax^2+bx+c=0")
a=float(input('enter coefficient of x^2'))
b=float(input('enter coefiicient of x'))
c=float(input('enter constant "c"'))
d=(b**2-(4*a*c))
e=d**(1/2)
if d<0:
    print("The roots are complex")
else:
    root1=(e-b)/(2*a)
    root2=(-e-b)/(2*a)
    print("The roots of equation are",root1 ,"and",root2)
