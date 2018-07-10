# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 07:59:29 2018

@author: allen
"""
#This code implements an algorithm for finding the nth Taylor coefficient
#########################################################
#The nth Taylor coefficient of a function f(x)
#Centered around x=a is given by 
#T_n=f^(n)(a)/n!
#It works best if f is infinitely differentiable at x=a.

#################################################################
#This code is all about finding the nth derivative of a function

#Import the appropriate libraries
#I am going to import sympy because this library will allow us to 
#symbolically take the derivative which will make things a lot easier.
#I'm also importing the symbolic variable x from sympy
#However there are other libraries that you should add here
import sympy as syp 
from sympy.abc import x


#Define the function of interest
def function(x):
	y=
	return y #Remember y is a local variable 

#I am going to write this bit of code for you to use in the program
#It will output the nth derivative of a function as a lambda function
#This will allow you to plug in values
def deriv(expr,n): #expr is a sympy function of x 
	              #The function of x is important. 
				    #All of my code here will assume that					
	symb_deriv=syp.diff(expr,'x',n)
	num_deriv=syp.lambdify(x,symb_deriv)
	return num_deriv

#Tests of the deriv function 
#Notice the form that I use to implement the function, f'(a)=deriv(f)(a)
print(deriv(x**2+2*x,2)(3))#This should return 2
print(deriv(syp.exp(2*x),1)(1))#This should return 14.7781

################################################

def Taylor_coeff(f,a,n): #here f is the function, a is the center of the series, and n is the term we want
	#You will need to make use of the function I coded, deriv
		
	
	return #return the value of the Taylor coefficient
	


