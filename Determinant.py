import numpy as np
import numpy.linalg as la
import math as m

# determine the determinant of a 2x2 matrix

def det1(a,b,c,d):
    determinant=a*d-b*c
    return determinant

def det2(a,b,c,d):
    A=np.matrix([[a,b],[c,d]])
    determinant=la.det(A)
    return determinant

print(det1(1,2,3,4))
print(det2(1,2,3,4))