'''
Use scipy.integrate.solve_ivp to solve the following initial value problems. In
each case, make a plot of the solution and argue why it is correct.
 y' = texp(3t) − 2y with 0 ≤ t ≤ 1 and y(0) = 0
 y' = 1 − (t − y)^2 with 2 ≤ t ≤ 3 and y(0) = 0
 y' = 1 + y/t with 1 ≤ t ≤ 2 and y(1) = 2
 y' = cos 2t + sin 3t with 0 ≤ t ≤ 1 and y(0) = 1

Find analytical solutions to these equations using a symbolic calculator (such as Math-
ematica or WolframAlpha) and put them on the plot.
'''
# Akashdeep Roy
import scipy.integrate as dd
import matplotlib.pyplot as plt
from numpy import *
h=0.01
def f(t,y):
    return t*exp(3*t)-2*y
def g(t,y):
    return 1-(t-y)**2
def h(t,y):
    return 1+(y/t)
def z(t,y):
    return (cos(2*t))+(sin(3*t))
def ftrue(t):
    return (1/25)*(exp(-2*t))*(1-exp(5*t)+5*t*exp(5*t)) 
def gtrue(t):
    return (t**2-3*t+1)/(t-3)
def htrue(t):
    return t*(2+log(t))
def ztrue(t):
    return (3*sin(2*t)-2*cos(3*t)+8)/6
sol=dd.solve_ivp(f,[0,1+0.01],[0],t_eval=arange(0,1+0.01,0.01))
pol=dd.solve_ivp(g,[2,3+0.01],[1],t_eval=arange(2,3+0.01,0.01))
dol=dd.solve_ivp(h,[1,2+0.01],[2],t_eval=arange(1,2+0.01,0.01))
zol=dd.solve_ivp(z,[0,1+0.01],[1],t_eval=arange(0,1+0.01,0.01))
p=sol.y[0]
plt.plot(sol.t,p,label='numerical')
plt.plot(sol.t,ftrue(sol.t),label='analytical')
plt.xlabel('t',size=18)
plt.ylabel('y',size=18)
plt.title('prob-7/a',size=16)
plt.grid()
plt.legend()
plt.show()
q=pol.y[0]
plt.plot(pol.t,q,label='numerical')
plt.plot(pol.t,gtrue(pol.t),label='analytical')
plt.xlabel('t',size=18)
plt.ylabel('y',size=18)
plt.title('prob-7/b',size=16)
plt.grid()
plt.legend()
plt.show()
r=dol.y[0]
plt.plot(dol.t,r,label='numerical')
plt.plot(dol.t,htrue(dol.t),label='analytical')
plt.xlabel('t',size=18)
plt.ylabel('y',size=18)
plt.title('prob-7/c',size=16)
plt.grid()
plt.legend()
plt.show()
s=zol.y[0]
plt.plot(zol.t,s,label='numerical')
plt.plot(zol.t,ztrue(zol.t),label='analytical')
plt.xlabel('t',size=18)
plt.ylabel('y',size=18)
plt.title('prob-7/d',size=16)
plt.grid()
plt.legend()
plt.show()