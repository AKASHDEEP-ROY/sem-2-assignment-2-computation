'''
Use the fourth order Runge-Kutta method to solve the initial value problem:
    u1'= u1+2*u2-2*u3+exp(-t)
    u2'= u2+u3-2*exp(-t)
    u3'= u1+2*u2+exp(-t)
with 0<t<1 , u1(0)=3, u2(0)=-1, u3(0)=1. Plot the results.
'''
#Akashdeep Roy
import numpy as np
import matplotlib.pyplot as plt

def f(u1,u2,u3,t):
    return u1 + 2*(u2-u3) + np.exp(-t)
def g(u1,u2,u3,t):
    return u2 + u3 - 2*np.exp(-t)
def s(u1,u2,u3,t):
    return u1 + 2*u2 + np.exp(-t)
h=0.01
t=np.arange(0,1+h,h)
u1=np.zeros(len(t),dtype=float)
u2=np.zeros(len(t),dtype=float)
u3=np.zeros(len(t),dtype=float)

u1[0]=3.00
u2[0]=-1.00
u3[0]=1.00
for i in range(len(t)-1):
    k1=h*f(u1[i],u2[i],u3[i],t[i])
    k2=h*f(u1[i]+k1/2,u2[i]+k1/2,u3[i]+k1/2,t[i]+h/2)
    k3=h*f(u1[i]+k2/2,u2[i]+k2/2,u3[i]+k2/2,t[i]+h/2)
    k4=h*f(u1[i]+k3,u2[i]+k3,u3[i]+k3,t[i]+h)
    k=(1/6)*(k1+k4+(2*(k2+k3)))
    u1[i+1]=u1[i]+k
 
    k1=h*g(u1[i],u2[i],u3[i],t[i])
    k2=h*g(u1[i]+k1/2,u2[i]+k1/2,u3[i]+k1/2,t[i]+h/2)
    k3=h*g(u1[i]+k2/2,u2[i]+k2/2,u3[i]+k2/2,t[i]+h/2)
    k4=h*g(u1[i]+k3,u2[i]+k3,u3[i]+k3,t[i]+h)
    k=(1/6)*(k1+k4+(2*(k2+k3)))
    u2[i+1]=u2[i]+k
    
    k1=h*s(u1[i],u2[i],u3[i],t[i])
    k2=h*s(u1[i]+k1/2,u2[i]+k1/2,u3[i]+k1/2,t[i]+h/2)
    k3=h*s(u1[i]+k2/2,u2[i]+k2/2,u3[i]+k2/2,t[i]+h/2)
    k4=h*s(u1[i]+k3,u2[i]+k3,u3[i]+k3,t[i]+h)
    k=(1/6)*(k1+k4+(2*(k2+k3)))
    u3[i+1]=u3[i]+k

plt.xlabel('t')
plt.ylabel('u(i)')  
plt.plot(t,u1,label='u_1')
plt.plot(t,u2,label='u_2')
plt.plot(t,u3,label='u_3')
plt.title('prob-11')
plt.grid()
plt.legend()
plt.show()