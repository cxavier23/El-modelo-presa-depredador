import numpy as np
from matplotlib import pyplot as plt

a, b, tau, k = 2.5E-4, 2.85E-3, 0.25, -5E-3
size, dx = 100, 0.2

T = 10.0
dt = 0.9 * (dx**2) / 2
n = int(T/dt)
U, V = np.random.rand(size, size), np.random.rand(size, size)

def Laplacian(Z):
	Ztop = Z[0:-2, 1:-1]
	Zleft = Z[1:-1, 0:-2]
	Zbottom = Z[2:, 1:-1]
	Zright = Z[1:-1, 2:]
	Zcenter = Z[1:-1, 1:-1]
	return (Ztop + Zleft + Zbottom + Zright - 4*Zcenter) / (dx**2)

for i in range(n):
	D2U = Laplacian(U)
	D2V = Laplacian(V)
	Uc = U[1:-1, 1:-1]
	Vc = V[1:-1, 1:-1]
	U[1:-1, 1:-1] = Uc + dt*(a*D2U-Vc+Uc-(Uc**3)+k)
	V[1:-1, 1:-1] = Vc + dt*(b*D2V+Uc-Vc) / tau

	for Z in (U,V):
		Z[0,:] = Z[1,:]
		Z[-1,:] = Z[-2,:]
		Z[:,0] = Z[:,1]
		Z[:,-1] = Z[:,-2]

plt.imshow(U, cmap = plt.cm.copper, extent = [-1,1,-1,1])
plt.xticks([])
plt.yticks([])
plt.show()