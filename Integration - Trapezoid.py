import matplotlib.pyplot as plot
import numpy as np
import math as m

xl=0
xu=12
n=1000

# Find the integral of a function
# Define function
def function(x):
    y=x**2
    return y

#Trapezoid Rule on function
def trapezoid(y,xl,xu,n):
    dx=(xu-xl)/n
    sum=0
    for i in range (0,n+1):
        if i==0 or i==n+1:
            trap=y(xl+i*dx)
            sum=sum+simp
        else:
            trap=2*y(xl+i*dx)
    return sum*.5*dx

def graph(y,xl,xu):
    x=np.arange(xl,xu,(xu-xl)/n)
    y=[]
    for xvals in x:
        y.append(y(xvals))
    plot.plot(xy)
    plot.grid(True)
    plot.xlabel("X")
    plot.ylabel("Y")
    plot.show()