# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 07:59:29 2018

@author: allen
"""
#This code implements the single variable Newtons Method
#########################################################
#Newtons method is an algorithm for solving an equation f(x)=0
#For any function f(x)
#The algorithm is as follows
#Step one: choose a point (normally close to the actual solution) x_0
#Step two: Find the value of the derivative f'(x_0)
#Step three: Find the equation of the tangent line, y=f'(x_0)(x-x_0)+f(x_0)
#Step Four: Solve the linear equation, 0=f'(x_0)(x-x_0)+f(x_0)
#Solution- x_1=(f'(x_0)x_0-f(x_0))/f'(x_0)
#Step Five: Repeat steps two through four for x_1 and so on

#################################################################
#There are two big pieces; finding the derivative and the iterative loop
#Hopefully you can use your other code for the derivative in this code
    #AJ I never got the other code for the derivative


#Import the appropriate libraries
import math as m
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp 
from sympy.abc import x

#Define the function of interest
def function(x):
    y=x**2-5  #how do i define this in a way that works well with my later functions?
    return y #Remember y is a local variable 

#Function for finding the derivative at x=a, f'(a)
def deriv(expr,n): #expr is the function and a is the value
    symb_deriv=sp.diff(expr,'x',n)
    numderiv=sp.lambdify(x,symb_deriv) #Again, dy is local and so if dy is used elsewhere it needs to be defined again
    return numderiv
    
print(deriv(x**2-5,1)(1))

def Newtons(f,x_initial,n): #here f is the function, x0 is the guess, and n is the number of loops 
    for i in range(n): #Loop the Newton's Method algorithm described in the beginning comments
        y_initial=function(x_initial)
        dy=deriv(function(x_initial),i)
        x_new=x_initial-y_initial/dy
        sol=x_new
    
    return y_initial #Sol is the approximation to the solution to f(x)=0
    
print(Newtons(function(x),1,100))
########################################################

#Print out test of code for each equation

#x^2+x-1=0, Solutions: -1.61803, 0.618034
    
#e^x-2=0, Solutions: 0.693147
    
#e^x-2x-5, Solutions: -2.45716, 2.25164
    
#sin(pi*x+3)-1=0 Funamental solution: -0.95493
