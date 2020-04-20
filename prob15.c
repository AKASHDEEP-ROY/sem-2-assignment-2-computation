/* Akashdeep Roy */


#include<stdio.h>
#include<stdlib.h>
#include<math.h>

float func(float y,float t)
{
return y-pow(t,2)+1;
}
int main()
{
int N,Flag;
float t,a,b,y,h,yt,err,eb;
a=0.0;
b=2.0;
h=0.2;
t=a;
y=0.5;
printf("\n    t\t\t y\t\ttrue solution\terror\t       error bound\n");
Flag=1;
while(Flag==1)

{

yt=pow((t+1),2)-0.5*exp(t);
err=fabs(y-yt);
eb=fabs(0.1*(0.5*exp(2)-2)*(exp(t)-1));
printf("%f\t%f\t   %f\t%f\t%f\n",t,y,yt,err,eb);
y=y+h*func(y,t);
t=t+h;
if(t>b)
{break;

}
}

}
