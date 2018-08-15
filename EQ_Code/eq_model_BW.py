# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 09:50:51 2018

@author: allen
"""

import sympy as syp 
import numpy as np
import scipy as scip
import scipy.integrate
import math as math 
import matplotlib.pyplot as plt

def Z_dot(D,A,beta,gamma,n,du,z0,t0,tf):
	dz=lambda t,z: (A*du-beta*abs(du)*pow(abs(z),n-1)*z-gamma*du*pow(abs(z),n))/D
	if tf==0:
		return 0
	else:
		sol = scip.integrate.solve_ivp(dz, (t0,tf),[z0],max_step=.01)
		return sol.y[0][-1]

def BW_EQModel(BWP,m,d,f,y0,tf,step):
	t=np.arange(0,tf,step)
	y=y0[0]
	dy=y0[1]
	z=0
	ti=t[0]
	ti_plus=t[1]
	sol=[y0[0]]
	hys_points=[BWP[0]*BWP[1]*y]
	for i in range(0,len(t)-2):
		z=Z_dot(BWP[2],BWP[3],BWP[4],BWP[5],BWP[6],dy,z,ti,ti_plus)
		Phi=BWP[0]*BWP[1]*y+(1-BWP[0])*BWP[2]*BWP[1]*z
		hys_points.append(Phi)
		def func_sys_iso(t,y):
			dy=[y[1],f(t)-Phi/m-d*y[1]/m]
			return dy
		sol_iso = scip.integrate.solve_ivp(func_sys_iso, (ti,ti_plus),[y, dy],max_step=step)
		ti=t[i+1]
		ti_plus=t[i+2]
		y=sol_iso.y[0][-1]
		dy=sol_iso.y[1][-1]
		sol.append(y)
		if ti_plus==t[-1]:
			z=Z_dot(BWP[2],BWP[3],BWP[4],BWP[5],BWP[6],dy,z,ti,ti_plus)
			Phi=BWP[0]*BWP[1]*y+(1-BWP[0])*BWP[2]*BWP[1]*z
			def func_sys_iso(t,y):
				dy=[y[1],f(t)+Phi/m-d*y[1]/m]
				return dy
			sol_iso = scip.integrate.solve_ivp(func_sys_iso, (ti,ti_plus),[y, dy],max_step=step)
			y=sol_iso.y[0][-1]
			dy=sol_iso.y[1][-1]
			sol.append(y)
			hys_points.append(Phi)
	def func_sys_niso(t,y):
		dy=[y[1],f(t)-BWP[1]*y[0]/m-d*y[1]/m]
		return dy
	sol_niso= scip.integrate.solve_ivp(func_sys_niso, (0,tf),y0,t_eval=t)
	f_points=[]
	for i in range(0,len(t)):
		f_points.append(f(t[i]))
	plt.plot(t,sol,'--',label='with Base Isolation')	
	#print(len(t),len(sol_niso.y[0]))
	plt.plot(t,sol_niso.y[0],label='without Base Isolation')
	#plt.plot(t,f_points)
	#plt.plot(sol,hys_points)
	#plt.plot(t,hys_points)
	plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
	plt.xlabel('time(sec)')
	plt.ylabel('displacement (m)')
	plt.savefig('Base_Isolation.png')
	return plt.show()

	