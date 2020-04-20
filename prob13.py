'''
Use Euler's method in a Python code to solve the initial value problem
t^2y"-2ty'+2y=t^3ln(t) with 1<t<2, y(1) = 1, and y'(1) = 0 with step size h = 0.001. Plot the solution
together with the known exact solution y(t) = 7t/4 + ((t^3)/2)ln(t) - (3/4)t^3
'''
#Akashdeep Roy
import numpy as np
import matplotlib.pyplot as plt
h=0.001
def f(y,ydot,t):
    return ((t**3)*np.log(t) - 2*y + 2*t*ydot)/(t**2)
def sol(t):
    return (7*t/4)+((t**3)/2)*np.log(t)-(3/4)*(t**3)
t=np.arange(1,2+h,h)
y=np.ones(len(t),dtype=float)
ydot=np.zeros(len(t),dtype=float)
ydot[0]=0.00

for i in range(len(t)-1):
    ydot[i+1]=ydot[i]+(h*f(y[i],ydot[i],t[i]))
    y[i+1]=y[i]+h*ydot[i]

plt.plot(t,y,label='numerical solution')
plt.plot(t,sol(t),label='analytical solution')
plt.xlabel('t')
plt.ylabel('y')
plt.title('prob-13')
plt.legend()
plt.show()
plt.plot(t,abs((sol(t)-y)/sol(t)))
plt.xlabel('t',size=18)
plt.ylabel('relative error',size=18)
plt.title('prob-13')
plt.show()

'''
Comment : Relative error makes an interesting curve with t.
'''