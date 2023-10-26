from matplotlib import pyplot as plt
import numpy as np
import pylab as py 
import random as rn
from scipy.integrate import odeint

colores = ["red", "blue", "yellow", "green",
					 "pink", "violet", "orange", "purple",
					 "cyan", "lime", "gold", "goldenrod",
					 "fuchsia", "silver", "palegreen", "darkkhaki",
					 "brown", "royalblue", "hotpink", "indigo", 
					 "orchid","darkorange", "tomato", "burlywood",
					 "teal", "coral", "navy", "olivedrab",
					 "sienna", "deeppink", "rebeccapurple", "slateblue",
					 "olive", "forestgreen", "magenta", "mediumspringgreen",
					 "tan", "darkred", "limegreen", "plum", 
					 "lightpink"]
c = len(colores)
col = rn.randint(0,c-1)

# Primer orden
def logistic(P,t,k,M):
	return k*P*(M-P)

# Segundo orden
def damped(y,t,m,c,k):
	x,v = y
	a = -(c*v + k*x) / m
	return np.array([v,a])

# Dos dimensiones
def predatorPrey(pp, t, a, p, b, q):
	x,y = pp
	dxdt = x*(a-p*y)
	dydt = y*(-b+q*x)
	return np.array([dxdt, dydt])

def brusselator(u,t,a,b):
	x,y = u
	dxdt = 1 - (1+b)*x + a*(x**2)*y
	dydt = b*x - a*(x**2)*y
	return [dxdt, dydt]


### LOGISTIC
#P0 = 1
#t = np.linspace(0,10)
#k = 0.1
#M = 10
#P = odeint(logistic, P0, t, args=(k,M))
#plt.plot(t, P, color = colores[col])
#plt.xlabel("Time")
#plt.ylabel("Population")
#plt.title("Logistic Population Growth")
#plt.show()

### DAMPED
#y0 = np.array([1, 0])
#t = np.linspace(0, 5, 200)
#m, c, k = 0.5, 1, 50
#y = odeint(damped, y0, t, args = (m, c, k))
#plt.plot(t, y[:,0], color = colores[col])
#plt.xlabel("Time")
#plt.ylabel("x(t)")
#plt.title("Damped Harmonic Motion")
#plt.show()

### PREDATOR-PREY
#pp0 = np.array([70, 10])
#t = np.linspace(0, 30, 200)
#a, p, b, q = 0.2, 0.005, 0.5, 0.01
#pp = odeint(predatorPrey, pp0, t, args = (a, p, b, q))
#plt.plot(t, pp[:,0], label = "Prey", color = colores[col])
#plt.plot(t, pp[:,1], label = "Predator", color = colores[(col+1)%c])
#plt.xlabel("Time")
#plt.ylabel("Populations")
#plt.title("Predator-Prey Model")
#plt.legend()
#plt.show()

### BRUSSELATOR
t = py.linspace(0.0, 100.0, 1000)
u0 = np.array([-1, 3.5])
a, b = 0.85, 1.80
u = odeint(brusselator, u0, t, args = (a, b))
#plt.plot(t, u[:,0], label = "Reagent X", color = colores[col])
#plt.plot(t, u[:,1], label = "Reagent Y", color = colores[(col+1)%c])
plt.plot(u[:,0], u[:,1], color = colores[(col+1)%c])
plt.xlabel("Time")
plt.ylabel("Concentrations")
plt.title("Brusselator")
#plt.legend()
plt.show()