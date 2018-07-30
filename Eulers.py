import math as m
import numpy as np
import matplotlib.pyplot as plt

#Euler's Method

def euler(t0,y0,n,tfinal):
    dt=(tfinal-t0)/n
    y=[]
    t=[]
    y.append(y0)
    t.append(t0)
    for i in range(t0,n)):
        t.append((i+1)*dt)
        y.append(y[i]+y[i]*t[i]*dt)
    return plt.plot(t,y)

print(euler(0,2,1000,10))