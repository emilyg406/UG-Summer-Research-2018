import numpy as np
import math as m

# find derivative of a function
def function(x):
    y=x**2
    return y

def derivative(x):
    f=x**2
    deriv=np.gradient(f)
    return f
