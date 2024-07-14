import numpy as np
import matplotlib.pyplot as plt
import numpy as np


def linspace(start, stop, step=1):
  return np.linspace(start, stop, int((stop - start) / step + 1))

def volumen_caja(x):
  return (200*(x)) - (60*((x)**2)) + (4*((x)**3))


x= linspace(2, 3, 0.05)
v= (200*(x)) - (60*((x)**2)) + (4*((x)**3))

L=2.11

punto= (200*(L)) - (60*((L)**2)) + (4*((L)**3))


plt.plot(x,v)
plt.scatter(L,punto, c='pink')

plt.show()
