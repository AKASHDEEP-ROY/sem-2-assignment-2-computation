'''
Implement the relaxation method for the boundary value problem in prob-5 in python
Make a plot that shows the exact solution, the numerical solution & at least five candidate solutions.
'''
# Akashdeep Roy
#print("I want to acknowledge Krishnendu for this coding. I have used his Gauss-Seidel code. My code that I have implemented in 1st assignment is not working here. I & Krishnendu were unable to find any error.")
import numpy as np
import matplotlib.pyplot as plt
h=0.2
t=np.arange(0,10+h,h)
g=-10
a=0
b=0
N=len(t)-2
A=[[0 for i in range (N)]for j in range(N)]
B=np.zeros(N)
for i in range(N):
    A[i][i]=-2
    for j in range(N):
        if(j==i-1):
            A[i][j]=1
        elif(j==i+1):
            A[i][j]=1
    B[i]=g*(h**2)
      
B[0]=(g-a)*(h**2)
B[len(t)-3]=(g-b)*(h**2)
#print(A,B,len(t))

def gauss_seidel(x):
    p=np.copy(x)
    x=np.zeros(N)
    for j in range(len(x)):       
       for k in range(len(x)):
           if k<j :
               x[j]=x[j]-(A[j][k]*x[k])
           if k>j:
                x[j]=x[j]-(A[j][k]*p[k])
       x[j]=(x[j]+B[j])/A[j][j]
    return x

X=[]
x=np.zeros(N)
Flag=1
c=0
while(Flag==1):
    z=np.zeros(len(t))
    for j in range(len(t)-2):
        z[j+1]=x[j]
    z[0]=0
    z[len(t)-1]=0
    X.append(z)
    p=np.copy(x)
    x=gauss_seidel(x)
    if(np.all(abs(x-p))<0.1):
        break    
    c+=1

plt.plot(t,X[c],"tab:red",label='actual solution')
plt.plot(t,X[int(c/10)],"tab:blue")
plt.plot(t,X[int(c/15)],"tab:blue")
plt.plot(t,X[int(c/20)],"tab:blue")
plt.plot(t,X[int(c/25)],"tab:blue")
plt.plot(t,X[int(c/30)],"tab:blue")
plt.xlabel("t",size=18)
plt.ylabel("x",size=18)
plt.title("Problem 6",size=16)
plt.legend()
plt.show()