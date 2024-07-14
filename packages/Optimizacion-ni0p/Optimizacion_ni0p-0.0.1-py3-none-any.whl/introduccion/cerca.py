import numpy as np
import matplotlib.pyplot as plt
import numpy as np


def linspace(start, stop, step=1):
  return np.linspace(start, stop, int((stop - start) / step + 1))

def ecuacion_cerca(x):
  return (200*(x)) - (8*((x)**2)/3)


x= linspace(-1, 4, 0.05)
v= ecuacion_cerca(x)
derivada= (200) - ((16/3)*x)

plt.plot(x,v)
plt.plot(x, derivada, c='pink')

plt.show()
