'''
use backward integration with Euler's method in a python code
to solve the following two initial-value problems:
    1. dy/dx=-9y, 0<=x<=1 , y(0)=e
    2. dy/dx=-20(y-x)^2+2x, 0<=x<=1 , y(0)=1/3
Do not use any integration functions from Numpy.
'''
# Akashdeep Roy
#Library import section
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
#given functions
def f(x,y):
    return -9*y
def g(x,y):
    return -20*(y-x)**2+2*x
#stepsize & mesh points
h=0.001
x=np.arange(0,1.0+h,h)
#initial value input
y=np.zeros(len(x),dtype=float)
z=np.zeros(len(x),dtype=float)
y[0]=np.exp(1)
z[0]=1/3
#guess for initialization of Newton-raphson to do backward integration
s=0
a=int(input('for first equ, press 1 ; for 2nd equ, press 2'))
#calculation section
for i in range(len(x)-1):
    def q(p):
        if(a==1):
           return p-y[i]-h*f(x[i+1],p)
        else:
           return p-z[i]-h*g(x[i+1],p)
    if(a==1):
        y[i+1]=optimize.newton(q,s)
    else:
        z[i+1]=optimize.newton(q,s)
if(a==2):
  for i in range(len(x)-1):
      y=z
#Output section
plt.xlabel('x',size=18)
plt.ylabel('y',size=18)
plt.plot(x,y)   #plot of numerical results
if(a==1):
  plt.title('Plot of numerical result for y(x) in prob 1/a',size=16)
else:
  plt.title('Plot of numerical result for y(x) in prob 1/b',size=16)
plt.grid()
plt.show()