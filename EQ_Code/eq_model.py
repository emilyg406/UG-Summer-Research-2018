# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 09:50:51 2018

@author: allen
"""

import sympy as syp 
import numpy as np
import scipy as scip
import math as math 
import matplotlib.pyplot as plt

def STD_EQModel(m,d,k,f,y0,tf,step):
	def func_sys(y,t):
		dy=[y[1],f(t)-k*y[0]/m-d*y[1]/m]
		return dy
	t = np.arange(0,tf, step)
	sol = scip.integrate.odeint(func_sys, [y0[0], y0[1]], t)
	t_sol=[]
	f_t=[]
	for i in range (0,len(t)):
		t_sol.append(sol[i][0])
		f_t.append(f(t[i]))
	plt.plot(t,f_t,label='Ground Motion')
	plt.plot(t,t_sol,'--',label='Building')
	plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
	plt.xlabel('time(sec)')
	plt.ylabel('displacement (m)')
	plt.savefig('SDOF_System.png')
	return plt.show()

	