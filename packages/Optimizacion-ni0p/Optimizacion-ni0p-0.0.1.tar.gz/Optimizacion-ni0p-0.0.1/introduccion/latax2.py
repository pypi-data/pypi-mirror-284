import numpy as np
import matplotlib.pyplot as plt
import numpy as np

def linspace(start, stop, step=1):
  return np.linspace(start, stop, int((stop - start) / step + 1))

def volumen_lata(r):
  return 2*3.1416*(r**2) + 500/r

r= linspace(0.5, 8, 0.1)
h= linspace(0.5, 8, 0.1)


sc= 2*3.1416*(r**2)
sl= 2*3.1416*r*h
S= 2*3.1416*(r**2) + 500/r

h1=250/(3.1416*(3.414**2))
#print("H:", h1)

#r1= np.sqrt((500/(4*3.1416)),3)
#print(r1)

plt.plot(r, S)

plt.show()
