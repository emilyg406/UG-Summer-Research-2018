from sympy.plotting import plot
from sympy import symbols
x = symbols('x')
graph=plot(x^2, title='Plot', xlabel='x', ylabel='y')
graph.show()
