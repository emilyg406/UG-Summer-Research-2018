# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 07:59:29 2018

@author: allen
"""
#This code implement solves an equation Ax=b directly.
#########################################################
#There are a couple of ways we could do this
#We could right a piece of code that would do Gaussian elimination
#On the system, but I think we should just make use of
#The linalg functions in NumPy
#################################################################
#To do this the fast easy way we'll do three things
#1. Check if det(A) is 0. If it is, then we won't be able to find the inverse matrix
#We'll ignore this case for now and return an error in the case
#2. Provided that A has an inverse, we find A^-1.
#3. Multiply B by A^-1 on the left.

#Import the appropriate libraries
import math
import matplotlib.pyplot as plt
import numpy as np

def LinearSolve(A,b): # A is a matrix, b is a vector)
    n=len(A)
    x=np.zeros(n)
    #Create an If statement that will return an appropriate error if det(A)=0
    if np.linalg.det(A)==0:
        return "Error - Determinant = 0"

    #Create an If statement that will return an appropriate error if the dimensions of A and b don't align
    elif len(A[0])!=len(b):
        return "Error: Incompatible dimensions"
    elif len(A)!=len(A[0]):
        return "Error: Incompatible Dimensions"

    #Find the inverse matrix A^-1
    else:
        Ainv=np.linalg.inv(A)

    #Multiply A^-1*b. Make sure this multiplication is in fact matrix times vector multiplication
    for i in range (0,n):
        for j in range (0,n):
            x[i]=x[i]+Ainv[i][j]*b[j]
            sol=x
    return sol #Return the solution vector 

print(LinearSolve([[4.523,7.23,7,8],[-3.1,4,5,2],[5,6,0.75,11],[-2,3,-1,4]],[1,2,3,4]))

########################################################

#Print out test of code for each equation

#A=[[1,2],[3,4]], b=[5,6] Solution:[-4,4.5]
    
#A=[[1,2,3],[4,5,6],[7,8,9]], b=[10,11,12] Solution: This will return an error, det(A)=0
    
#A=[[4,5,7,8],[3,4,5,2],[5,6,7,11],[-2,3,-1,4]], b=[3,4,5,-1,3] Solution: This will return an error, A and b are different sizes
    
#A=[[4.523,7.23,7,8],[-3.1,4,5,2],[5,6,0.75,11],[-2,3,-1,4]], b=[1,2,3,4] Solution: [-0.331268,1.06199,-0.609205,-0.114425]