from matplotlib import pyplot as plt
import numpy as np
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
col = np.random.randint(0,c-1)


def predatorPrey(pp, t, a, p, b, q):
	x,y = pp
	dxdt = x*(a-p*y)
	dydt = y*(-b+q*x)
	return np.array([dxdt, dydt])

def solutionPlot(t, pp, t_data, prey_data, predator_data, Titulo):
	plt.plot(t_data, prey_data, label = "Prey", color = colores[col])
	plt.plot(t_data, predator_data, label = "Predator", color = colores[(col+1)%c])

	#plt.plot(t, pp[:,0], color = colores[(col+2) % c], label = "Prey - Teorico")
	#plt.plot(t, pp[:,1], color = colores[(col+3) % c], label = "Pedator - Teorico")
	
	plt.scatter(t_data, prey_data, color = colores[col])
	plt.scatter(t_data, predator_data, color = colores[(col+1)%c])

	plt.xticks([2*i for i in range(11)])
	plt.xlabel("Tiempo (minutos)")
	plt.ylabel("Poblacion")
	plt.title(Titulo + " - Evolucion Temporal")
	plt.legend()
	plt.show()

def phasePlot(pp, prey_data, predator_data, Titulo):
	plt.plot(prey_data, predator_data, color = colores[col])
	
	plt.scatter(prey_data, predator_data, color = colores[col])

	#plt.plot(pp[:,0], pp[:,1], color = colores[(col+1)%c], label = "Modelo Teorico")
	
	plt.xlabel("Presas")
	plt.ylabel("Depredadores")
	plt.title(Titulo + " - Retrato Fase")
	#plt.legend()
	plt.show()



op = 7

if op == 1:
	Titulo = "Juego 1"
	MuePresas = np.array([2,5,0,0,0,0,0,0,0,0])
	MueDepredadores = np.array([3,1,0,0,0,0,0,0,0,0])
	NacPresas = np.array([3,0,0,0,0,0,0,0,0,0])
	NacDepredadores = np.array([1,1,0,0,0,0,0,0,0,0])
	pp0 = np.array([6,6])
elif op == 2:
	Titulo = "Juego 2"
	MuePresas = np.array([5,0,0,0,0,0,0,0,0,0])
	MueDepredadores = np.array([1,0,0,0,0,0,0,0,0,0])
	NacPresas = np.array([0,0,0,0,0,0,0,0,0,0])
	NacDepredadores = np.array([0,0,0,0,0,0,0,0,0,0])
	pp0 = np.array([5,7])
elif op == 3:
	Titulo = "Juego 3"
	MuePresas = np.array([1,1,0,0,5,2,1,0,1,0])
	MueDepredadores = np.array([1,2,1,4,2,0,1,0,0,0])
	NacPresas = np.array([1,1,2,1,1,1,1,1,1,0])
	NacDepredadores = np.array([0,0,0,2,2,2,0,0,2,0])
	pp0 = np.array([8,6])
elif op == 4:
	Titulo = "Juego 4 - Girls Only"
	MuePresas = np.array([1,0,0,0,0,0,0,0,0,0])
	MueDepredadores = np.array([3,0,0,0,0,0,0,0,0,0])
	NacPresas = np.array([0,0,0,0,0,0,0,0,0,0])
	NacDepredadores = np.array([0,0,0,0,0,0,0,0,0,0])
	pp0 = np.array([4,3])
elif op == 5:
	Titulo = "Juego 5"
	MuePresas = np.array([5,3,1,3,3,1,4,3,1,5])
	MueDepredadores = np.array([2,5,2,0,1,0,1,0,0,2])
	NacPresas = np.array([0,1,2,2,2,2,2,2,2,3])
	NacDepredadores = np.array([0,2,1,1,1,1,1,1,1,2])
	pp0 = np.array([12,12])
elif op == 6:
	Titulo = "Juego 6"
	MuePresas = np.array([2,5,4,0,1,2,1,4,2,5])
	MueDepredadores = np.array([3,1,2,5,2,2,1,0,2,2])
	NacPresas = np.array([0,3,2,2,2,2,2,2,2,4])
	NacDepredadores = np.array([0,1,1,1,1,2,2,1,1,1])
	pp0 = np.array([12,13])
elif op == 7:
	Titulo = "Juego 7"
	MuePresas = np.array([7,0,1,1,0,0,0,0,0,0])
	MueDepredadores = np.array([4,0,4,3,2,2,0,0,0,0])
	NacPresas = np.array([0,0,2,2,2,2,0,0,0,0])
	NacDepredadores = np.array([0,0,1,3,1,1,0,0,0,0])
	pp0 = np.array([9,9])
else:
	print(":(")
	quit()

	

prey_data = [pp0[0]]
predator_data = [pp0[1]]
for i in range(len(NacPresas)):
	prey_data.append(prey_data[i] + NacPresas[i] - MuePresas[i])
	predator_data.append(predator_data[i] + NacDepredadores[i] - MueDepredadores[i])

t = np.linspace(0, 20, 200)
a = np.mean(NacPresas)/2
p = np.mean(MuePresas)/2
b = np.mean(MueDepredadores)/2
q = np.mean(NacDepredadores)/2
pp = odeint(predatorPrey, pp0, t, args = (a, p, b, q))

t_data = np.arange(0, 2*(len(MuePresas)+1), 2)
prey_data = np.array(prey_data)
predator_data = np.array(predator_data)

#solutionPlot(t, pp, t_data, prey_data, predator_data, Titulo)
phasePlot(pp, prey_data, predator_data, Titulo)