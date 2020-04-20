'''
Use Euler's method in a python code to approximate the solution for
the initial value problem :
    y'=(y/t)-(y/t)^2  1<=t<=2  y(1)=1
Use a step size of h=0.1
We know using analytical methods that the solution to above equation is :
    y = t/(1+ln(t))
Compute the absolute and relative error in the solution.
'''
#Akashdeep Roy
import numpy as np
import matplotlib.pyplot as plt
def f(t,y):
    return (y/t)-(y/t)**2
def sol(t):
    return t/(1+np.log(t))
h=0.1
t=np.arange(1.0,2.0+h,h)
y=np.zeros(len(t),dtype=np.float)
y[0]=1
for i in range(len(t)-1):
    y[i+1]=y[i]+h*f(t[i],y[i])
plt.title('Solution of prob-2',size=16)
plt.plot(t,y,label='Euler method solution')
plt.plot(t,sol(t),label='Analytical solution')
plt.legend()
plt.xlabel('t',size=18)
plt.ylabel('y',size=18)
plt.show()
plt.title('Absolute Error with t, prob-2',size=16)
plt.plot(t,abs(sol(t)-y))
plt.xlabel('t',size=18)
plt.ylabel('Absolute Error',size=18)
plt.show()
plt.title('Relative Error with t, prob-2',size=16)
plt.plot(t,abs(sol(t)-y)/sol(t))
plt.xlabel('t',size=18)
plt.ylabel('Relative error',size=18)
plt.show()

'''
Comment : Behaviour of Relative error is amazing. It increases sharply just after t=1 but decreases smoothly with t.
          but absolute error is increasing always.
'''