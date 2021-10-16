# THE LAW OF LARGE NUMBERS
# Gaussian fitting for random variables in python

print('---------------------------------------------------------------------------------------------------------------------')

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from random import gauss


def percentage(d):
    # d=len(list)
    ans = (d*100)/n
    print('Random variables in range -1 to 1 :-',d)
    print('Expected Percentage :- 68.2 %')
    print('Percentage :-',ans,'%')


mu,sd = 0,1
a, b = mu-3*sd, mu+3*sd
x=np.linspace(a,b,1000)
y=norm.pdf(x,loc=mu,scale=sd)
glist=[]
list=[]
n=int(input('Enter n:-'))


for i in range(n):
    c=gauss(mu,sd)
    glist.append(c)
    if c < 1 and c > -1:
        plt.scatter(c,0.20)
    elif (c<2 and c>1) or (c>-2 and c<-1):
        plt.scatter(c,0.05)
    else:
        plt.scatter(c,0.00)

for i in glist:
    if i >= -1 and i <= 1:
        list.append(i)
d=len(list)

percentage(d)


plt.plot(x,y,'.r')
plt.axvline(x=0)
plt.axvline(x=-1)
plt.axvline(x=1)
plt.axvline(x=-2)
plt.axvline(x=2)
plt.axvline(x=-3)
plt.axvline(x=3)
plt.show()

print('---------------------------------------------------------------------------------------------------------------------')
