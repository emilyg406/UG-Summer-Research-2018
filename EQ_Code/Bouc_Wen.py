# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 09:39:07 2018

@author: allen
"""

import sympy as syp 
import numpy as np
import scipy as scip
import scipy.integrate
import math as math 
import matplotlib.pyplot as plt


def BW_Model(beta,gamma,n,u,loops):
	t_vals = np.arange(0,loops*2*math.pi,.0001)
	du=lambda t: scip.misc.derivative(u, t, dx=1e-8)
	dz=lambda t,z: -2*du(t)-beta*abs(du(t))*pow(abs(z),n-1)*z-gamma*du(t)*pow(abs(z),n)
	sol = scip.integrate.solve_ivp(dz, (0,loops*2*math.pi),[0],max_step=.01)
	return [sol.t,sol.y]
u=lambda t: 7.5*math.sin(t)
ki=2
a=0.5
sol=BW_Model(0.5,0,1.1,u,3)
u_points=[]
f_points=[]
for i in range (0,len(sol[0])):
	u_points.append(u(sol[0][i]))
	f_points.append(a*ki*u_points[i]+(1-a)*ki*sol[1][0][i])
plt.plot(u_points,f_points)
plt.show()

