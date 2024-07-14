import numpy  as np
import matplotlib.pyplot as plt

# --------------------------------- FUNCIONES ---------------------------------
def caja(l):
    return 4*(l)**3 - 60*(l)**2 + 200*l

def lata(r):
    return 2 * np.pi * (r**2)  + 500/r

def fun1(x):
    return ((x**2) +  54)/x

def fun2(x):
    return (x**3) + (2*x) - (3)

def fun3(x):
    return (x**4) + (x*2) - 33

def fun4(x):
    return (3*(x**4)) - (8*(x**3)) - (6*(x**2)) + (12*x)

def calcular_n(a, b, precision):
    return int((b - a) / precision)

def exhaustive_search(a, b, precision, funcion):
    n = calcular_n(a, b, precision)
    delta_x = (b - a) / n # precision
    x1 = a
    x2 = x1 + delta_x
    x3 = x2 + delta_x
    puntos = [] # puntos evaluados
    while x3 <= b:
        if funcion(x1) >= funcion(x2) <= funcion(x3):
            return (x1, x3), puntos
        else:
            x1 = x2
            x2 = x3
            x3 = x2 + delta_x
            puntos.append((x2, funcion(x2))) 
    return None, puntos

def graficar(precisiones, x, y, a, b, nombre_funcion, funcion):
    plt.plot(x, y, label='Función {}'.format(nombre_funcion))

    # Graficar los puntos devueltos por exhaustive_search para cada precisión
    for i, precision in enumerate(precisiones):
        punto_final, _ = exhaustive_search(a, b, precision, funcion)
        if punto_final is not None:
            x_punto, _ = punto_final
            plt.scatter(x_punto, funcion(x_punto), label=f'Precision {precision}', c=f'C{i}')

    # Configuraciones adicionales
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Búsqueda Exhaustiva - {}'. format(nombre_funcion))
    plt.legend()
    plt.grid(True)
    plt.show()

# --------------------------- PARAMETROS -------------------------------

# ---- Función Lata                   0.5 < x <= 10
a = 0.5
b = 10
precisiones = [0.5, 0.1, 0.01, 0.0001]
x = np.linspace(a, b, 200)
y = lata(x) 

graficar(precisiones, x, y, a, b, 'Lata', lata)

# --- Función Caja                   2 < x <= 3.5
a = 2
b = 10
precisiones = [0.5, 0.1, 0.01, 0.0001]
y = caja(x) 

graficar(precisiones, x, y, a, b, 'Caja', caja)

# --- Función (x^2 + 54) / x         0 < x <= 10
a = 0.1
b = 10
precisiones = [0.5, 0.1, 0.01, 0.0001]
y = fun1(x) 

graficar(precisiones, x, y, a, b, '(x^2+54)/x', fun1)

# --- Función x^3 + 2x - 3           -5 < x <= 5  
a = -5
b = 5
precisiones = [0.5, 0.1, 0.01, 0.0001]
y = fun2(x) 

graficar(precisiones, x, y, a, b, 'x^3+2x-3', fun2)

# --- Función x^4 + x^2 - 33         -2.5 <= x <= 2.5
a = -2.5
b = 2.5
precisiones = [0.5, 0.1, 0.01, 0.0001]
y = fun3(x) 

graficar(precisiones, x, y, a, b, 'x^4+x^2-33 ', fun3)

# --- Función 3x^4 - 8x^3 -6x^2 + 12x          -1.5 <= x <= 3
a = -1.5
b = 3
precisiones = [0.5, 0.1, 0.01, 0.0001]
y = fun4(x) 

graficar(precisiones, x, y, a, b, '3x^4-8x^3-6x^2+12x', fun4)