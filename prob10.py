'''
Solve the initial value problem using 4th order Runge-Kutta method:
    dx/dt = 1/(x^2+t^2) , 0<t<inf , x(0)=1
What is the value of the solution at t=3.5*10^6 ?
'''
#Akashdeep Roy
from numpy import *
from matplotlib import pyplot as plt

y=[] # y corresponding to t
z=[] # z corresponding to y
#defining the ODE
def f(t,x):
    return 1/(x**2+t**2)    
# Set initial conditions.
t = 0
x = 1
y.append(t)
z.append(x)
# Set initial step size.
h = 1e-1
# Set minimal step size.
dt_min = 1e-4
# Set relative change tolerances.
dx_max = 0.01  # Enables faster speed.
dx_min = 0.0008 # Controls accuracy.
tol = 1e-4
while (t < 5*10**6):
    # 
    k1 = h*f(t,x)
    k2 = h*f(t+h/2,x+k1/2)
    k3 = h*f(t+h/2,x+k2/2)
    k4 = h*f(t+h,x+k3)
    k =  (1/6)*(k1+k4+ 2*(k2+k3))
    x1 = x + k
    # Calculate partial steps.
    k1 = (h/2)*f(t,x)
    k2 = (h/2)*f(t+h/4, x+k1/4)
    k3 = (h/2)*f(t+h/4, x+k2/4)
    k4 = (h/2)*f(t+h/2, x+k3/2)
    k = 1/6*(k1+2*k2+2*k3+k4)
    x2 = x + k
    # Calculate partial steps.
    k1 = 2*h*f(t,x)
    k2 = 2*h*f(t+h,x+k1/2)
    k3 = 2*h*f(t+h,x+k2/2)
    k4 = 2*h*f(t+(2*h),x+k3)
    k = (1/6)*(k1+2*k2+2*k3+k4)
    x3 = x + k
    
    if (abs(x1) < tol): # Use a fixed step size for small values of x.
        if (h != dt_min):
            h = dt_min
            x0 = x1
    else:
        if (abs(x1)>tol and abs(x1-x2)/abs(x1)>dx_max):
            h = h/2 # Error is too large; decrease step size.
            x0 = x2
        elif (abs(x1)>tol and abs(x1-x2)/abs(x1)<dx_min):
            h = h*2 # Larger error is acceptable; increase step size.
            x0 = x3
        else:
            x0 = x1 # This step size is just right.
    y.append(t+h)
    x = x0
    z.append(x)
    t = t + h
    if(3.5*(10**6)-t<h and 3.5*(10**6)-t>0):
        h0=3.5*(10**6)-t
        k1 = h0*f(t,x)
        k2 = h0*f(t+h0/2,x+k1/2)
        k3 = h0*f(t+h0/2,x+k2/2)
        k4 = h0*f(t+h0,x+k3)
        k =  (1/6)*(k1+k4+ 2*(k2+k3))
        x1 = x + k
        print("value of x at t=3.5e6 is ",x1)
plt.title('prob-10')
plt.plot(y,z,'tab:blue',label='solid line')
plt.plot(y,z,'ro',markersize=2,label='mesh points')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()