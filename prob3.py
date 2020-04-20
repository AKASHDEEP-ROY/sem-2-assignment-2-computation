'''
Use the Runge-Kutta Method in python code to solve the differential equation:
    y"-2y'+y=xexp(x)-x , 0<x<1 , y(0)=0 , y'(0)=0
'''
# Akashdeep Roy
from numpy import *
import matplotlib.pyplot as plt
def f(x,y,ydot):
    return 2*ydot-y-x+x*exp(x)
def g(x,y,ydot):
    return ydot
h=0.01
x=arange(0.0,1.0+h,h)
y=zeros(len(x),dtype=float)
ydot=zeros(len(x),dtype=float)

for i in range(len(x)-1):
    k1=h*f(x[i],y[i],ydot[i])
    k2=h*f(x[i]+h/2,y[i]+k1/2,ydot[i]+k1/2)
    k3=h*f(x[i]+h/2,y[i]+k2/2,ydot[i]+k2/2)
    k4=h*f(x[i]+h,y[i]+k3,ydot[i]+k3)
    k=(1/6)*(k1+k4+(2*(k2+k3)))
    ydot[i+1]=ydot[i]+k
    
    k1=h*g(x[i],y[i],ydot[i])
    k2=h*g(x[i]+h/2,y[i]+k1/2,ydot[i]+k1/2)
    k3=h*g(x[i]+h/2,y[i]+k2/2,ydot[i]+k2/2)
    k4=h*g(x[i]+h,y[i]+k3,ydot[i]+k3)
    k=(1/6)*(k1+k4+(2*(k2+k3)))
    y[i+1]=y[i]+k

plt.plot(x,y)
plt.xlabel('x',size=18)
plt.ylabel('y',size=18)
plt.title('prob-3',size=16)
plt.grid()
plt.show()
plt.plot(x,ydot)
plt.xlabel('x',size=18)
plt.ylabel('dy/dx',size=18)
plt.title('prob-3',size=16)
plt.grid()
plt.show()