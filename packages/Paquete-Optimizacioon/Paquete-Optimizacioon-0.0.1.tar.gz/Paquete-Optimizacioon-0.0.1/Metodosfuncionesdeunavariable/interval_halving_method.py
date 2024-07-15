import numpy as np
import matplotlib.pyplot as plt

def linspace(start, stop, step=0.05):
    """
    Genera un array de números equidistantes entre start y stop con un tamaño de paso especificado.

    Parámetros:
    start (float): El valor inicial de la secuencia.
    stop (float): El valor final de la secuencia.
    step (float): El tamaño del paso entre valores consecutivos. Por defecto es 0.05.

    Retorna:
    numpy.ndarray: Array de números equidistantes.
    """
    return np.linspace(start, stop, int((stop - start) / step + 1))

def caja(l):
    """
    Calcula el volumen de una caja en función de su longitud.

    Parámetros:
    l (float): La longitud de la caja.

    Retorna:
    float: El volumen calculado de la caja.
    """
    return -1 * (4 * (l)**3 - 60 * (l)**2 + 200 * l)

def lata(r):
    """
    Calcula el área superficial de una lata en función de su radio.

    Parámetros:
    r (float): El radio de la lata.

    Retorna:
    float: El área superficial calculada de la lata.
    """
    return 2 * np.pi * (r**2) + 500 / r

def f1(x):
    """
    Calcula el valor de la función f1 en el punto x.

    Parámetros:
    x (float): El valor en el que se evalúa la función.

    Retorna:
    float: El valor calculado de la función.
    """
    return (x**2) + 54 / x

def f2(x):
    """
    Calcula el valor de la función f2 en el punto x.

    Parámetros:
    x (float): El valor en el que se evalúa la función.

    Retorna:
    float: El valor calculado de la función.
    """
    return (x**3) + (2 * x) - 3

def f3(x):
    """
    Calcula el valor de la función f3 en el punto x.

    Parámetros:
    x (float): El valor en el que se evalúa la función.

    Retorna:
    float: El valor calculado de la función.
    """
    return (x**4) + (x**2) - 33

def f4(x):
    """
    Calcula el valor de la función f4 en el punto x.

    Parámetros:
    x (float): El valor en el que se evalúa la función.

    Retorna:
    float: El valor calculado de la función.
    """
    return (3 * (x**4)) - (8 * (x**3)) - (6 * (x**2)) + 12 * x

# Arreglos con los límites generados para cada función
lim_lata = linspace(0.5, 8)
lim_caja = linspace(2, 3)
lim_f1 = linspace(0, 10)
lim_f2 = linspace(0, 5)
lim_f3 = linspace(-2.5, 2.5)
lim_f4 = linspace(-1.5, 3)

def interval_halving(a, b, epsilon, f):
    """
    Implementa el método de bisección de intervalos para encontrar el mínimo de una función.

    Parámetros:
    a (float): El límite inferior del intervalo.
    b (float): El límite superior del intervalo.
    epsilon (float): La precisión deseada para la ubicación del mínimo.
    f (function): La función a minimizar.

    Retorna:
    tuple: Una tupla que contiene el punto estimado del mínimo y el punto anterior.
    """
    L = b - a
    xm = (a + b) / 2
    f_xm = f(xm)
    x_ant = None  # Inicializamos x_ant como None porque no hay valor anterior en la primera iteración

    while L > epsilon:
        L = L / 2
        x1 = a + L / 4
        x2 = b - L / 4
        f_x1 = f(x1)
        f_x2 = f(x2)

        x_ant = xm  # Guardamos el valor actual de xm antes de actualizarlo

        if f_x1 < f_xm:
            b = xm
            xm = x1
            f_xm = f_x1
        elif f_x2 < f_xm:
            a = xm
            xm = x2
            f_xm = f_x2
        else:
            a = x1
            b = x2

    return (xm, x_ant)  # Devolvemos tanto xm como el valor anterior x_ant

print(interval_halving(0.6, 5, 0.5, lata))

# Calcular puntos para cada función
puntos_lata1 = interval_halving(0.6, 5, 0.5, lata)
puntos_lata2 = interval_halving(0.6, 5, 0.1, lata)
puntos_lata3 = interval_halving(0.6, 5, 0.01, lata)
puntos_lata4 = interval_halving(0.6, 5, 0.0001, lata)

puntos_caja1 = interval_halving(2, 3, 0.5, caja)
puntos_caja2 = interval_halving(2, 3, 0.1, caja)
puntos_caja3 = interval_halving(2, 3, 0.01, caja)
puntos_caja4 = interval_halving(2, 3, 0.0001, caja)

puntos_f11 = interval_halving(0.6, 5, 0.5, f1)
puntos_f12 = interval_halving(0.6, 5, 0.1, f1)
puntos_f13 = interval_halving(0.6, 5, 0.01, f1)
puntos_f14 = interval_halving(0.6, 5, 0.0001, f1)

puntos_f21 = interval_halving(0.6, 5, 0.5, f2)
puntos_f22 = interval_halving(0.6, 5, 0.1, f2)
puntos_f23 = interval_halving(0.6, 5, 0.01, f2)
puntos_f24 = interval_halving(0.6, 5, 0.0001, f2)

puntos_f31 = interval_halving(-2, 2.5, 0.5, f3)
puntos_f32 = interval_halving(-2, 2.5, 0.1, f3)
puntos_f33 = interval_halving(-2, 2.5, 0.01, f3)
puntos_f34 = interval_halving(-2, 2.5, 0.0001, f3)

puntos_f41 = interval_halving(-1.8, 2.5, 0.5, f4)
puntos_f42 = interval_halving(-1.8, 2.5, 0.1, f4)
puntos_f43 = interval_halving(-1.8, 2.5, 0.01, f4)
puntos_f44 = interval_halving(-1.8, 2.5, 0.0001, f4)

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
plt.subplot

(233)
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
plt.scatter(puntos_f21, puntos_f21, label='Delta=0.5', marker='o')
plt.scatter(puntos_f22, puntos_f22, label='Delta=0.1', marker='o')
plt.scatter(puntos_f23, puntos_f23, label='Delta=0.01', marker='o')
plt.scatter(puntos_f24, puntos_f24, label='Delta=0.0001', marker='o')
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