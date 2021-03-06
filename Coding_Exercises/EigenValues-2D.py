# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 07:59:29 2018

@author: allen
"""
#This code finds the eigenvalues and eigenvectors for a 2x2 matrix, [[a,b],[c,d]]
#########################################################
#1. Solve the characteristic equation x^2-(a+d)x+(ad-bc)
#2. Solve the equation (A-lambda*I)x=0
    #Since A-lambda*I is not invertible this would normally be tricky
    #But since we are dealing with a 2x2 system, being non-invertible
    #Is equivalent to the columns of the matrix being multiples of each other
    #Thus we can assume that x=[1,a] for some constant a
#3. Normalize both of the eigenvectors, i.e. reduce them so they have norm equal to 1    
#################################################################
#One important thing to note here is that we might have complexe solutions
#This is fine we want to include them in our answer
#You'll need to figure out how to appropriately do this.


#Import the appropriate libraries
import numpy as np
import math as m

def EVal(A): # A is a 2x2 matrix
    
    #Create an If statement that will return an appropriate error if A is not 2x2
    if len(A)!=2:
        sol="Matrix A is not 2x2 - cannot determine eigenvalues"
    elif len(A[0])!=2:
        sol="Matrix A is not 2x2 - cannot determine eigenvalues"
    elif len(A[1])!=2:
        sol="Matrix A is not 2x2 - cannot determine eigenvalues"
    
    #Solve the characteristic equation
    else:
        a=1
        b=-A[0][0]-A[1][1]
        c=(A[0][0]*A[1][1])-(A[0][1]*A[1][0])
        dis=b**2-4*a*c
        if dis>=0:
            #Find a solution to (A-lambda*I)x=0 for both solutions
            #Normalize your solutions
            lambda1=(-b+np.sqrt(dis))/2
            lambda2=(-b-np.sqrt(dis))/2
            
            if A[0][0]-lambda1==0 and A[1][0]==0:
                v1=np.aray([0,1])
            else:
                v1=np.array([-A[0][1]/(A[0][0]-lambda1),1])

            if A[0][0]-lambda2==0 and A[1][0]==0:
                v2=np.array([0,1])
            else:
                v2=np.array([-A[0][1]/(A[0][0]-lambda2),1])

            v1_mag=m.sqrt(v1[0]**2+v1[1]**2)
            v2_mag=m.sqrt(v2[0]**2+v2[1]**2)
            v1_norm=v1/v1_mag
            v2_norm=v2/v2_mag
            sol=[lambda1,v1_norm],[lambda2,v2_norm]
        
        else:
            re=-b/2
            im=(np.sqrt(-dis))/2
            lambda1=np.complex(re,im)
            lambda2=np.complex(re,-im)

            if A[0][0]-lambda1==0 and A[1][0]==0:
                v1=np.aray([0,1])
            else:
                v1=np.array([-A[0][1]/(A[0][0]-lambda1),1])

            if A[0][0]-lambda2==0 and A[1][0]==0:
                v2=np.array([0,1])
            else:
                v2=np.array([-A[0][1]/(A[0][0]-lambda2),1])

            sol=[lambda1,v1],[lambda2,v2]
    
    #Return the solution in the form [lambda_1,v_1],[lambda_2,v_2]
    return sol

print(EVal([[4,5,13],[3,4,5],[5,6,7]]))
    
########################################################

#Print out test of code for each equation

#A=[[1,2],[3,4], Solution: [-5.37228,[0.415974, 0.909377]], [0.372281,[-0.824565, 0.565767]]
    
#A=[[0,1],[-1,0]],Solution: complex solutions [i,[- 0.707107i, 0.707107],[-i,[0.707107i, 0.707107]]

#A=[[4,5,13],[3,4,5],[5,6,7]], Should return an error

