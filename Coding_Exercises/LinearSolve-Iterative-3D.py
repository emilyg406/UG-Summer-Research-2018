# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 07:59:29 2018

@author: allen
"""
#This code implement solves an equation Ax=b iteratively where A is 3x3.
#########################################################
#An iterative solver means that we first guess a solution
#Then proceed through a number of steps to more accurately approximate the solution
#Newton's Method is an iterative solver.
##############################################################
#Here is the process we will use
#First we solve and get x,y,and z in terms of the other variables
#For instance if A=[[1,2,1],[3,4,5],[-1,0,2]] and b=[3,7,10]
#Then x=3-2y-z, y=(7-3x-5z)/3, and z=10+x
#Then we plug in our guess and iterate 
#x_(k+1)=3-2y_k-z_k, y_(k+1)=(7-3x_k-5z_k)/3, and z_(k+1)=10+x_k
#
#We loop as many times until we have a desired accuracy |[x_(k+1),y_(k+1),z_(k+1)]-[x_k,y_k,z_k]|<e
#################################################################


#Import the appropriate libraries
import math as m
import numpy as np
import matplotlib.pyplot as plt

def LinearSolveIt(A,b): # A is a 3x3 matrix, b is a vector    A=np.array()

    #Create an If statement that will return an appropriate error if det(A)=0
    if abs(np.linalg.det(A))<10**-8:
        sol="Error: Determinant equals zero"
    
    #Create an If statement that will return an appropriate error if the dimensions of A and b don't align
    elif len(A)!=len(b):
        sol="Error: Dimensions not compatible"
    
    else:   
        #Create a guess that will be used. This way the user doesn't have to input one
        x_initial=0
        y_initial=0
        z_initial=0

        x_new=-1
        y_new=1
        z_new=-1
        #Define an appropriate error for the solution
        maxerror=0.0001
        count=0
        #Create a while loop that runs the iteration while |[x_(k+1),y_(k+1),z_(k+1)]-[x_k,y_k,z_k]|<e
        while abs(x_new-x_initial)>maxerror and abs(y_new-y_initial)>maxerror and abs(z_new-z_initial)>maxerror:
            
            x_initial=x_new
            y_initial=y_new
            z_initial=z_new
            
            x_new=(b[0]-A[0][1]*y_initial-A[0][2]*z_initial)/A[0][0]
            y_new=(b[1]-A[1][0]*x_new-A[1][2]*z_initial)/A[1][1]
            z_new=(b[2]-A[2][0]*x_new-A[2][1]*y_new)/A[2][2]
            count=count+1
            
            sol=[x_new,y_new,z_new]
            #You should create a break statement in your while loop. This will prevent the loop from running forever
            if count>=1/maxerror**2:
                sol=[x_new,y_new,z_new] 
                break    #is only looping around once - how do I fix this? 
            
    return sol #Return the solution vector 

print(LinearSolveIt([[8,5,1],[3,24,5],[5,6,15]],[1,2,3]))
    
########################################################

#Print out test of code for each equation

#A=[[1,2,3],[4,5,6],[7,8,9]], b=[10,11,12] Solution: This will return an error, det(A)=0
    
#A=[[4,5,7],[3,4,5],[5,6,7]], b=[3,4,5,-1,3] Solution: This will return an error, A and b are different sizes
    
#A=[[4,5,13],[3,4,5],[5,6,7]], b=[1,2,3] Solution: [-0.214286, 0.928571, -0.214286]

