import numpy as np
import matplotlib.pyplot as plt 

def linspace(start, stop, step=0.05):
    return np.linspace(start, stop, int((stop - start) / step + 1))

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

def golden_search(a, b, epsilon, f):
    aw = 0
    bw = 1
    Lw = bw - aw
    
    # Inicializamos w1 y w2 con valores dentro del intervalo normalizado [aw, bw]
    w1 = aw + 0.618 * Lw
    w2 = bw - 0.618 * Lw

    # Evaluamos la función en los puntos iniciales w1 y w2
    f1 = f(w1)
    f2 = f(w2)

    while Lw > epsilon:
        if f1 < f2:
            bw = w2
            w2 = w1
            Lw = bw - aw
            w1 = aw + 0.618 * Lw
            f2 = f1
            f1 = f(w1)
        else:
            aw = w1
            w1 = w2
            Lw = bw - aw
            w2 = bw - 0.618 * Lw
            f1 = f2
            f2 = f(w2)
    
    return aw, bw

print(golden_search(0.6, 7, 0.5,f1))

# Calcular puntos para cada función
puntos_lata1 = golden_search(0.6, 5, 0.5, lata)
puntos_lata2 = golden_search(0.6, 5, 0.1, lata)
puntos_lata3 = golden_search(0.6, 5, 0.01, lata)
puntos_lata4 = golden_search(0.6, 5, 0.0001, lata)

puntos_caja1 = golden_search(2, 3, 0.5, caja)
puntos_caja2 = golden_search(2, 3, 0.1, caja)
puntos_caja3 = golden_search(2, 3, 0.01, caja)
puntos_caja4 = golden_search(2, 3, 0.0001, caja)

puntos_f11 = golden_search(0.6, 5, 0.5, f1)
puntos_f12 = golden_search(0.6, 5, 0.1, f1)
puntos_f13 = golden_search(0.6, 5, 0.01, f1)
puntos_f14 = golden_search(0.6, 5, 0.0001, f1)

puntos_f21 = golden_search(0.6, 5, 0.5, f2)
puntos_f22 = golden_search(0.6, 5, 0.1, f2)
puntos_f23 = golden_search(0.6, 5, 0.01, f2)
puntos_f24 = golden_search(0.6, 5, 0.0001, f2)

puntos_f31 = golden_search(-2, 2.5, 0.5, f3)
puntos_f32 = golden_search(-2, 2.5, 0.1, f3)
puntos_f33 = golden_search(-2, 2.5, 0.01, f3)
puntos_f34 = golden_search(-2, 2.5, 0.0001,f3)

puntos_f41 = golden_search(-1.8, 2.5, 0.5, f4)
puntos_f42 = golden_search(-1.8, 2.5, 0.1, f4)
puntos_f43 = golden_search(-1.8, 2.5, 0.01,f4)
puntos_f44 = golden_search(-1.8, 2.5, 0.0001,f4)

# Grafica resultados
plt.figure(figsize=(12, 8))

# Grafica función lata
plt.subplot(231)
plt.plot(lim_lata, lata(lim_lata), label='Función')
plt.scatter(puntos_lata1[0], lata(puntos_lata1[0]), label='Delta=0.5', marker='o')
plt.scatter(puntos_lata2[0], lata(puntos_lata2[0]), label='Delta=0.1', marker='o')
plt.scatter(puntos_lata3[0], lata(puntos_lata3[0]), label='Delta=0.01', marker='o')
plt.scatter(puntos_lata4[0], lata(puntos_lata4[0]), label='Delta=0.0001', marker='o')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función Lata')
plt.legend()
plt.grid(True)

# Grafica función caja
plt.subplot(232)
plt.plot(lim_caja, caja(lim_caja), label='Función')
plt.scatter(puntos_caja1[0], caja(puntos_caja1[0]), label='Delta=0.5', marker='o')
plt.scatter(puntos_caja2[0], caja(puntos_caja2[0]), label='Delta=0.1', marker='o')
plt.scatter(puntos_caja3[0], caja(puntos_caja3[0]), label='Delta=0.01', marker='o')
plt.scatter(puntos_caja4[0], caja(puntos_caja4[0]), label='Delta=0.0001', marker='o')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función Caja')
plt.legend()
plt.grid(True)

# Grafica función f1
plt.subplot(233)
plt.plot(lim_f1, f1(lim_f1), label='Función')
plt.scatter(puntos_f11[1], f1(puntos_f11[1]), label='Delta=0.5', marker='o')
plt.scatter(puntos_f12[1], f1(puntos_f12[1]), label='Delta=0.1', marker='o')
plt.scatter(puntos_f13[1], f1(puntos_f13[1]), label='Delta=0.01', marker='o')
plt.scatter(puntos_f14[1], f1(puntos_f14[1]), label='Delta=0.0001', marker='o')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función f1')
plt.legend()
plt.grid(True)

# Grafica función f2
plt.subplot(234)
plt.plot(lim_f2, f2(lim_f2), label='Función')
plt.scatter(puntos_f21[0], puntos_f21[0], label='Delta=0.5', marker='o')
plt.scatter(puntos_f22[0], puntos_f22[0], label='Delta=0.1', marker='o')
plt.scatter(puntos_f23[0], puntos_f23[0], label='Delta=0.01', marker='o')
plt.scatter(puntos_f24[0], puntos_f24[0], label='Delta=0.0001', marker='o')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función f2')
plt.legend()
plt.grid(True)

# Graficar función f3
plt.subplot(235)
plt.plot(lim_f3, f3(lim_f3), label='Función')
plt.scatter(puntos_f31[1], f3(puntos_f31[1]), label='Delta=0.5', marker='o')
plt.scatter(puntos_f32[1], f3(puntos_f32[1]), label='Delta=0.1', marker='o')
plt.scatter(puntos_f33[0], f3(puntos_f33[0]), label='Delta=0.01', marker='o')
plt.scatter(puntos_f34[1], f3(puntos_f34[1]), label='Delta=0.0001', marker='o')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función f3')
plt.legend()
plt.grid(True)

# Graficar función f4
plt.subplot(236)
plt.plot(lim_f4, f4(lim_f4), label='Función')
plt.scatter(puntos_f41[1], f4(puntos_f41[1]), label='Delta=0.5', marker='o')
plt.scatter(puntos_f42[1], f4(puntos_f42[1]), label='Delta=0.1', marker='o')
plt.scatter(puntos_f43[1], f4(puntos_f43[1]), label='Delta=0.01', marker='o')
plt.scatter(puntos_f44[1], f4(puntos_f44[1]), label='Delta=0.0001', marker='o')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función f4')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()