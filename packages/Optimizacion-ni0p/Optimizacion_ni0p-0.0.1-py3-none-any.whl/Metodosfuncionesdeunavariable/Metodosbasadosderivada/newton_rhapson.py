import numpy as np
import matplotlib.pyplot as plt 

def linspace(start, stop, step=0.05):
    return np.linspace(start, stop, int((stop - start) / step + 1))

#Basadas en Central Difference Method (Scarborough, 1966)
def derivada(f, x, deltaa_x):
    return (f(x + deltaa_x) - f(x - deltaa_x)) / (2 * deltaa_x)

def segunda_derivada(f, x, deltaa_x):
    return (f(x + deltaa_x) - 2 * f(x) + f(x - deltaa_x)) / (deltaa_x ** 2)

def delta_x(x):
    if abs(x) > 0.01:
        return 0.01 * abs(x)
    else:
        return 0.0001

#Funciones 
def caja(l):
    return -1*(4*(l)**3 - 60*(l)**2 + 200*l)

def lata(r):
    return 2 * np.pi * (r**2)  + 500/r

def f1(x):
    return ((x)**2) + 54/x

def f2(x):
    return ((x)**3) + (2*(x)) - 3

def f3(x):
    return ((x)**4) + ((x)**2) - 33

def f4(x):
    return (3*((x)**4)) - (8*((x)**3)) - (6*((x)**2)) + 12*(x)

#Arreglos con los límites generados para cada función
lim_lata = linspace(0.5, 8)
lim_caja = linspace(2, 3)
lim_f1 = linspace(0, 10)
lim_f2 = linspace(0, 5)
lim_f3 = linspace(-2.5, 2.5)
lim_f4 = linspace(-1.5, 3)

def newton_method(x0, epsilon, f):
    x = x0
    while abs(derivada(f, x, delta_x(x))) > epsilon:
        segunda_deriv = segunda_derivada(f, x, delta_x(x))
        if segunda_deriv == 0:
            return x
        x = x - derivada(f, x, delta_x(x)) / segunda_deriv
    return x

print(newton_method(0.6, 0.5,f1))

# Calcular puntos para cada función
puntos_lata1 = newton_method(0.6, 0.5, lata)
puntos_lata2 = newton_method(0.6, 0.1, lata)
puntos_lata3 = newton_method(0.6, 0.01, lata)
puntos_lata4 = newton_method(0.6, 0.0001, lata)

puntos_caja1 = newton_method(2, 0.5, caja)
puntos_caja2 = newton_method(2, 0.1, caja)
puntos_caja3 = newton_method(2, 0.01, caja)
puntos_caja4 = newton_method(2, 0.0001, caja)

puntos_f11 = newton_method(0.6, 0.5, f1)
puntos_f12 = newton_method(0.6, 0.1, f1)
puntos_f13 = newton_method(0.6, 0.01, f1)
puntos_f14 = newton_method(0.6, 0.0001, f1)

'''
puntos_f21 = newton_method(0.6, 0.5, f2)
puntos_f22 = newton_method(0.6, 0.1, f2)
puntos_f23 = newton_method(0.6, 0.01, f2)
puntos_f24 = newton_method(0.6, 0.0001, f2)
'''

puntos_f31 = newton_method(-2, 0.5, f3)
puntos_f32 = newton_method(-2, 0.1, f3)
puntos_f33 = newton_method(-2, 0.01, f3)
puntos_f34 = newton_method(-2, 0.0001,f3)

puntos_f41 = newton_method(-1.8, 0.5, f4)
puntos_f42 = newton_method(-1.8, 0.1, f4)
puntos_f43 = newton_method(-1.8, 0.01,f4)
puntos_f44 = newton_method(-1.8, 0.0001,f4)

# Grafica resultados
plt.figure(figsize=(12, 8))

# Grafica función lata
plt.subplot(231)
plt.plot(lim_lata, lata(lim_lata), label='Función')
plt.scatter(puntos_lata1, lata(puntos_lata1), label='Delta=0.5', marker='o')
plt.scatter(puntos_lata2, lata(puntos_lata2), label='Delta=0.1', marker='o')
plt.scatter(puntos_lata3, lata(puntos_lata3), label='Delta=0.01', marker='o')
plt.scatter(puntos_lata4, lata(puntos_lata4), label='Delta=0.0001', marker='o')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función Lata')
plt.legend()
plt.grid(True)

# Grafica función caja
plt.subplot(232)
plt.plot(lim_caja, caja(lim_caja), label='Función')
plt.scatter(puntos_caja1, caja(puntos_caja1), label='Delta=0.5', marker='o')
plt.scatter(puntos_caja2, caja(puntos_caja2), label='Delta=0.1', marker='o')
plt.scatter(puntos_caja3, caja(puntos_caja3), label='Delta=0.01', marker='o')
plt.scatter(puntos_caja4, caja(puntos_caja4), label='Delta=0.0001', marker='o')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función Caja')
plt.legend()
plt.grid(True)

# Grafica función f1
plt.subplot(233)
plt.plot(lim_f1, f1(lim_f1), label='Función')
plt.scatter(puntos_f11, f1(puntos_f11), label='Delta=0.5', marker='o')
plt.scatter(puntos_f12, f1(puntos_f12), label='Delta=0.1', marker='o')
plt.scatter(puntos_f13, f1(puntos_f13), label='Delta=0.01', marker='o')
plt.scatter(puntos_f14, f1(puntos_f14), label='Delta=0.0001', marker='o')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función f1')
plt.legend()
plt.grid(True)

'''
# Grafica función f2
plt.subplot(234)
plt.plot(lim_f2, f2(lim_f2), label='Función')
plt.scatter(puntos_f21, puntos_f21, label='Delta=0.5', marker='o')
plt.scatter(puntos_f22, puntos_f22, label='Delta=0.1', marker='o')
plt.scatter(puntos_f23, puntos_f23, label='Delta=0.01', marker='o')
plt.scatter(puntos_f24, puntos_f24, label='Delta=0.0001', marker='o')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función f2')
plt.legend()
plt.grid(True)
'''

# Graficar función f3
plt.subplot(235)
plt.plot(lim_f3, f3(lim_f3), label='Función')
plt.scatter(puntos_f31, f3(puntos_f31), label='Delta=0.5', marker='o')
plt.scatter(puntos_f32, f3(puntos_f32), label='Delta=0.1', marker='o')
plt.scatter(puntos_f33, f3(puntos_f33), label='Delta=0.01', marker='o')
plt.scatter(puntos_f34, f3(puntos_f34), label='Delta=0.0001', marker='o')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función f3')
plt.legend()
plt.grid(True)

# Graficar función f4
plt.subplot(236)
plt.plot(lim_f4, f4(lim_f4), label='Función')
plt.scatter(puntos_f41, f4(puntos_f41), label='Delta=0.5', marker='o')
plt.scatter(puntos_f42, f4(puntos_f42), label='Delta=0.1', marker='o')
plt.scatter(puntos_f43, f4(puntos_f43), label='Delta=0.01', marker='o')
plt.scatter(puntos_f44, f4(puntos_f44), label='Delta=0.0001', marker='o')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función f4')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()