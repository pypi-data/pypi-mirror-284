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

# Genera los primeros n números de Fibonacci
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[-1] + fib[-2])
    return fib

def fibonacci_search(a, b, n, precision, f):
    fib = fibonacci(n)  # Generar los números de Fibonacci hasta n
    k = 2
    L = b - a
    x1 = a + (fib[n - k - 1] / fib[n - k + 1]) * L
    x2 = a + (fib[n - k] / fib[n - k + 1]) * L
    
    # Evaluaciones iniciales de la función
    f1 = f(x1)
    f2 = f(x2)
    
    while k < n and abs(b - a) > precision:
        if f1 > f2:
            a = x1
            x1 = x2
            x2 = a + (fib[n - k] / fib[n - k + 1]) * L
            f1 = f2
            f2 = f(x2)
        else:
            b = x2
            x2 = x1
            x1 = a + (fib[n - k - 1] / fib[n - k + 1]) * L
            f2 = f1
            f1 = f(x1)
        k += 1
        L = b - a
    # Devolver los dos últimos valores de x calculados
    return (x1, x2)

print(fibonacci_search(0.6, 7, 50, 0.5,f1))

# Calcular puntos para cada función
puntos_lata1 = fibonacci_search(0.6, 5, 50, 0.5, lata)
puntos_lata2 = fibonacci_search(0.6, 5, 50, 0.1, lata)
puntos_lata3 = fibonacci_search(0.6, 5, 50, 0.01, lata)
puntos_lata4 = fibonacci_search(0.6, 5, 50, 0.0001, lata)

puntos_caja1 = fibonacci_search(2, 3, 50, 0.5, caja)
puntos_caja2 = fibonacci_search(2, 3, 50, 0.1, caja)
puntos_caja3 = fibonacci_search(2, 3, 50, 0.01, caja)
puntos_caja4 = fibonacci_search(2, 3, 50, 0.0001, caja)

puntos_f11 = fibonacci_search(0.6, 5, 50, 0.5, f1)
puntos_f12 = fibonacci_search(0.6, 5, 50, 0.1, f1)
puntos_f13 = fibonacci_search(0.6, 5, 50, 0.01, f1)
puntos_f14 = fibonacci_search(0.6, 5, 50, 0.0001, f1)

puntos_f21 = fibonacci_search(0.6, 5, 50, 0.5, f2)
puntos_f22 = fibonacci_search(0.6, 5, 50, 0.1, f2)
puntos_f23 = fibonacci_search(0.6, 5, 50, 0.01, f2)
puntos_f24 = fibonacci_search(0.6, 5, 50, 0.0001, f2)

puntos_f31 = fibonacci_search(-2, 2.5, 50, 0.5, f3)
puntos_f32 = fibonacci_search(-2, 2.5, 50, 0.1, f3)
puntos_f33 = fibonacci_search(-2, 2.5, 50, 0.01, f3)
puntos_f34 = fibonacci_search(-2, 2.5, 50, 0.0001,f3)

puntos_f41 = fibonacci_search(-1.8, 2.5, 50, 0.5, f4)
puntos_f42 = fibonacci_search(-1.8, 2.5, 50, 0.1, f4)
puntos_f43 = fibonacci_search(-1.8, 2.5, 50, 0.01,f4)
puntos_f44 = fibonacci_search(-1.8, 2.5, 50, 0.0001,f4)

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
plt.scatter(puntos_f21[1], puntos_f21[1], label='Delta=0.5', marker='o')
plt.scatter(puntos_f22[1], puntos_f22[1], label='Delta=0.1', marker='o')
plt.scatter(puntos_f23[1], puntos_f23[1], label='Delta=0.01', marker='o')
plt.scatter(puntos_f24[1], puntos_f24[1], label='Delta=0.0001', marker='o')
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