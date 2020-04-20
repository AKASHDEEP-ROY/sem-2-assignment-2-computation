'''
Use scipy.integrate.solve_bvp to solve the following BVP. 
In each case, make a plot of the solution and argue why it is correct.
y"=-exp(-2y) , 1<x<2 , y(1)=0 , y(2)=ln(2)
y"=y'cos(x)-yln(y) , 0<x<pi/2 , y(0)=1 , y(pi/2)=e
y"=-(2(y')^3 +(y^2).y')sec(x) , pi/4<x<pi/3 , y(pi/4)=2^-0.25 , y(pi/3)=0.5*12^0.25
y"=0.5-0.5(y')^2-y.sin(x/2) , 0<x<pi , y(0)=2 , y(pi)=2
Find analytical solutions to these equations using mathematica & put them on the plot.
'''
# Akashdeep Roy
print("I would like to acknowledge Krishnendu who has made me understand its documentation.")
from scipy.integrate import solve_bvp as bvp
import matplotlib.pyplot as plt
import numpy as np
#1st problem
a=1     
b=2
def fun(x,y):          
    return np.vstack((y[1],-np.exp(-2*y[0])))
def bc(ya,yb):        
    return np.array([ya[0],yb[0]-np.log(2)])
x=np.linspace(a,b,100)       
y=np.zeros((2,x.size))
y[0]=1              
sol=bvp(fun,bc,x,y)         
y1=np.loadtxt("bvp1.txt",usecols=0)      
plt.plot(x,sol.sol(x)[0],label="numerical result")
plt.plot(x,y1,label="analytical")
plt.legend()
plt.xlabel("x",size=18)
plt.ylabel("y",size=18)
plt.title("Problem 8-a",size=18)
plt.show()
#2nd problem
a=0
b=np.pi/2
def fun(x,y):
    return np.vstack((y[1],y[1]*np.cos(x)-y[0]*np.log(y[0])))
def bc(ya,yb):
    return np.array([ya[0]-1,yb[0]-np.exp(1)])
x=np.linspace(a,b,100)       
y=np.zeros((2,x.size))
y[0]=1              
sol=bvp(fun,bc,x,y)         
y1=np.loadtxt("bvp2.txt",usecols=0)      
plt.plot(x,sol.sol(x)[0],label="numerical result")
plt.plot(x,y1,label="analytical")
plt.legend()
plt.xlabel("x",size=18)
plt.ylabel("y",size=18)
plt.title("Problem 8-b",size=18)
plt.show()
# 3rd problem
a=np.pi/4
b=np.pi/3
def fun(x,y):
    return np.vstack((y[1],-(2*(y[1])**3 +(y[0]**2)*y[1])/np.cos(x)))
def bc(ya,yb):
    return np.array([ya[0]-(2**(-0.25)),yb[0]-(0.5*(12**0.25))])
x=np.linspace(a,b,100)       
y=np.zeros((2,x.size))
y[0]=1              
sol=bvp(fun,bc,x,y)         
y1=np.loadtxt("bvp3.txt",usecols=0)      
plt.plot(x,sol.sol(x)[0],label="numerical result")
plt.plot(x,y1,label="analytical")
plt.legend()
plt.xlabel("x",size=18)
plt.ylabel("y",size=18)
plt.title("Problem 8-c",size=18)
plt.show()
# 4th problem
a=0
b=np.pi
def fun(x,y):
    return np.vstack((y[1],(1/2)*(1-y[1]**2-y[0]*np.sin(x))))
def bc(ya,yb):
    return np.array([ya[0]-2,yb[0]-2])
x=np.linspace(a,b,100)       
y=np.zeros((2,x.size))
y[0]=1              
sol=bvp(fun,bc,x,y)         
y1=np.loadtxt("bvp4_crt.txt",usecols=0)      
plt.plot(x,sol.sol(x)[0],label="numerical result")
plt.plot(x,y1,label="analytical")
plt.legend()
plt.xlabel("x",size=18)
plt.ylabel("y",size=18)
plt.title("Problem 8-d",size=18)
plt.show()