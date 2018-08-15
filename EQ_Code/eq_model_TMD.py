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


def TMD_EQModel(m,xsi,omega,f,y0,tf,step):
	def func_sys(y,t):
		dy=[y[1],f(t)/m[0]-2*xsi[0]*omega[0]*y[1]-pow(omega[0],2)*y[0]+(m[1]/m[0])*(2*xsi[1]*omega[1]*y[3]+pow(omega[1],2)*y[2]),y[3],-f(t)/m[0]+2*xsi[0]*omega[0]*y[1]+pow(omega[0],2)*y[0]-(1+(m[1]/m[0]))*(2*xsi[1]*omega[1]*y[3]+pow(omega[1],2)*y[2])]
		return dy
	def func_sys_nd(y,t):
		dy=[y[1],f(t)/m[0]-pow(omega[0],2)*y[0]-2*xsi[0]*omega[0]*y[1]]
		return dy
	t = np.arange(0, tf, step)
	sol = scip.integrate.odeint(func_sys,y0, t)
	sol_n=scip.integrate.odeint(func_sys_nd,[y0[0],y0[1]], t)
	t_sol1=[]
	t_sol2=[]
	t_soln=[]
	f_t=[]
	for i in range (0,len(t)):
		t_sol1.append(sol[i][0])
		t_sol2.append(sol[i][2])
		t_soln.append(sol_n[i][0])
		f_t.append(f(t[i]))
		
	#plt.plot(t,f_t)
	plt.plot(t,t_sol1,'--', label='with TMD')
	#plt.plot(t,t_sol2,':')
	plt.plot(t,t_soln,'-.', label='without TMD')
	plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
	plt.xlabel('time(sec)')
	plt.ylabel('displacement (m)')
	plt.savefig('Tuned_Mass_Damper.png')
	return plt.show()

	