# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 07:59:29 2018

@author: allen
"""
#This code finds the least squares fit line for a set of 2-variable data
#The plots the line and data on a graph
#########################################################
#The least squares fit line f(x)=ax+b is the line 
#Such that the least squares error, sqrt(sum((f(x_k)-y_k)^2)/n) is minimized
#You can find the parameters of the line a and b of the line ax+b
#By minimizing a multivariable function
#You can look up the formulas for a and b online
#The formulas are a bit complicated to include in this comment
#################################################################
#The big thing in this assignment is that the user should be able
#To input any length of two-variable data.
#That means that you won't know beforehand the size of the number of data points
#
#The next big snag is computing the numbers a and b
#Since we don't know the size of the data set, you will need to 
#Make sure the code works for any size of data. 
#The constants a and b also involve a large sum
#So unless there is a function in numpy, you will need to create a couple of 
#different loops for these calculations


#Import the appropriate libraries
import numpy as np
import math as m
import matplotlib.pyplot as plot

def LeastSquares_line(data): #data should be a list of two variable data ,i.e. [[4,5],[-1,2],[2,2],[-1,3],[10,0]]
    n=len(data) #Create a constant for the size of the data
    x=[]
    y=[]
    xsquare=[]
    xy=[]
    for i in range(0,n):
        x.append(data[i][0]) #Create a list or array of the first coordinates of the data    
        y.append(data[i][1]) #Create a list or array of the second coordinates of the data    
        #Both the average of the x values and y values appear in the equations for a and b     
        xsquare.append((x[i])**2) #Calculate the sum of the squares of the x values
        xy.append((x[i])*(y[i])) #Calculate the sum of x_k*y_k
    sum_xy=sum(xy)
    sum_xsquare=sum(xsquare)
    sumx_square=(sum(x))**2      
    sumx=sum(x)
    sumy=sum(y)
    #You should now have all of the constants you need to calculate a and b
    denom=n*sum_xsquare-sumx_square
    a=(sumy*sum_xsquare-sumx*sum_xy)/denom
    b=(n*sum_xy-sumx*sumy)/denom
    
    #Plot the data and the least squares fit line.
    t=np.arange(0,10,0.2)
    bestfit=plot.plot(t,b*t+a)
    graph=plot.plot(x,y,'ro')
    return graph, a, b

    #Be sure to make the plot include all of the data
    #As well as distinguish the color of your data from the line
    #Finally you should include the equation of the line in the plot

print(LeastSquares_line([[1, 2], [1.7, 6], [7, 6], [1.7, 4], [2, 3], [5, 6]]))

    
########################################################

#Print out test of code for each equation

#data=[[1, 2], [1.7, 6], [7, 6], [1.7, 4], [2, 3], [5, 6]] Solution:2.96414 + 0.500823 x
    
#data=[[-1, 2], [1.7, -3], [7, 0], [3, -5.7], [-2, 3]] Solution:     0.074665 - 0.468198 x
    
#data=create a random set of two variable data that ranges from 0 to 100 with 5000 entries