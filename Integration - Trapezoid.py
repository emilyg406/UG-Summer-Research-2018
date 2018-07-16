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
def trapezoid(xl,xu,n):
    dx=(xu-xl)/n
    sum=0
    for i in range (0,n+1):
        if i==0 or i==n+1:
            trap=function(xl+i*dx) 
            sum=sum+trap
        else:
            trap=2*function(xl+i*dx)
            sum=sum+trap
    return sum*.5*dx

print(trapezoid(0,5,10000)) 