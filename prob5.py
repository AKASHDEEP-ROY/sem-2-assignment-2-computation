'''
Implement the shooting method in python for the boundary value problem:
    d2x/dt2=-g where g=10
Boundary conditions are given as:
    x=0 at t=0    x=0 at t=t1=10
Can you use numpy.argmin to find the solution? 
Make a plot that shows the exact solution, the numerical solution, and at least five candidate solutions.
'''
#Akashdeep Roy
from numpy import *
import matplotlib.pyplot as plt
g=10
h=0.01
t1=10
a=0
b=100
xend=0
err=0.01
t=arange(0,t1+h,h)
x=ones(len(t),dtype=float)
v=zeros(len(t),dtype=float)
while(abs(x[len(t)-1]-xend)>err):
    s=(a+b)/2
    x[0]=0
    v[0]=s
    
    for i in range(len(t)-1):
        v[i+1]=v[i]+h*(-g)
        x[i+1]=x[i]+h*v[i]
    if(x[len(t)-1]<xend):
        a=s
    elif(x[len(t)-1]>xend):
        b=s      
    plt.plot(t,x,'tab:blue')
plt.plot(t,x,'tab:red',label='the actual solution')
plt.xlabel('t',size=18)
plt.ylabel('x',size=18)
plt.title('prob-5',size=16)
plt.legend()
plt.grid()
plt.show()