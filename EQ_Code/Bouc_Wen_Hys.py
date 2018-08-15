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


def BW_HYS(BWP,loops):
	u=lambda t: math.sin(t)
	a=BWP[0]
	k=BWP[1]
	D=BWP[2]
	A=BWP[3]
	beta=BWP[4]
	gamma=BWP[5]
	n=BWP[6]
	#t_vals = np.arange(0,loops*2*math.pi,.0001)
	du=lambda t: scip.misc.derivative(u, t, dx=1e-8)
	dz=lambda t,z: (A*du(t)-beta*abs(du(t))*pow(abs(z),n-1)*z-gamma*du(t)*pow(abs(z),n))/D
	sol = scip.integrate.solve_ivp(dz, (0,loops*2*math.pi),[0],max_step=.01)
	u_points=[]
	f_points=[]
	for i in range (0,len(sol.y[0])):
		u_points.append(u(sol.t[i]))
		f_points.append(a*k*u_points[i]+(1-a)*D*k*sol.y[0][i])
	plt.plot(u_points,f_points)
	plt.grid()
	plt.xlabel('Displacement')
	plt.ylabel('Restoring Force')
	plt.savefig('BoucWen_Hyteresis.png')
	return plt.show()


