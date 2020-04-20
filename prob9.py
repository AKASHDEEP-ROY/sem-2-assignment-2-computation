'''
In a python code, use adaptive step-size control with the fourth-order Runge-Kutta Method to solve:
    y' = (y^2 + y)/t , 1<t<3 , y(1)=-2
The absolute accuracy of the solution should be better than 10^-4.
Make a plot showing the solution and the mesh points.
'''
# Akashdeep Roy
from numpy import *
import matplotlib.pyplot as plt
def f(y,t):
    return ((y**2)+y)/t
h=0.1
T=[1]
Y=[-2]
y=-2
t=1
u=-2
v=1
q=10**(-4)
while(v<=3.00):
# mesh point using h
  k1=h*f(y,t)
  k2=h*f(y+k1/2,t+h/2)
  k3=h*f(y+k2/2,t+h/2)
  k4=h*f(y+k3,t+h)
  k=(1/6)*(k1+k4+(2*(k2+k3)))
  y1=y+k
# mesh point using h/2 running twice by j-loop
  for j in range(1):  
    k1=(h/2)*f(y,t)
    k2=(h/2)*f(y+k1/2,t+h/4)
    k3=(h/2)*f(y+k2/2,t+h/4)
    k4=(h/2)*f(y+k3,t+h/2)
    k=(1/6)*(k1+k4+(2*(k2+k3)))
    y=y+k
    t=t+(h/2)
  y2=y
# adaptive step size = hm
  hm=h*(q*h*30/abs(y1-y2))**0.25
# mesh point using hm
  k1=hm*f(u,v)
  k2=hm*f(u+k1/2,v+hm/2)
  k3=hm*f(u+k2/2,v+hm/2)
  k4=hm*f(u+k3,v+hm)
  k=(1/6)*(k1+k4+(2*(k2+k3)))
  u=u+k
  y=u #saving in y to calculate mesh points using h in next step
  Y.append(u)
  v=v+hm
  t=v #saving in t to calculate mesh points using h in next step
  T.append(v)
O=zeros(len(T),dtype=float) # To plot mesh points
plt.plot(T,Y,label='solution')
plt.title('prob-9')
plt.xlabel('t',size=18)
plt.ylabel('y',size=18)
plt.plot(T,O,"ro",markersize=2,label='mesh points')
plt.legend()
plt.show()