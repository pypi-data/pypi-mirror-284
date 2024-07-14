import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import random

def linspace(start, stop, step=1):
  return np.linspace(start, stop, int((stop - start) / step + 1))

#v=250 
#V= pi*r^2*h=250
r= linspace(0.5, 8, 0.2)
h= linspace(0.5, 8, 0.2)

r1, h2 = np.meshgrid(r, h)

sc= 2*3.1416*(r1**2)
sl= 2*3.1416*r1*h2
S= sc + sl #= ((2*np.pi())*(r**2)) + 2*np.pi()*r*h
S_copia= S

for i in range(0,9):
    for j in range(0,9):
        if S_copia[i,j]!=250:
            S_copia[i,j]=0

print(S_copia)

#plot 2d
plt.scatter(r1, h2, c=S)

#plot3d
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax1 = fig.add_subplot(projection='3d')
ax.scatter(r1, h2, S, cmap='viridis')
ax1.scatter(r1, h2, S_copia, cmap='viridis')

plt.show()
