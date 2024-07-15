import numpy as np
import matplotlib.pyplot as plt

def linspace(start, stop, step=0.05):
    """
    Genera una secuencia de números espaciados uniformemente.

    Args:
        start (float): El valor inicial de la secuencia.
        stop (float): El valor final de la secuencia.
        step (float, opcional): El tamaño del paso entre los valores. Por defecto es 0.05.

    Returns:
        np.ndarray: Una matriz de valores espaciados uniformemente.
    """
    return np.linspace(start, stop, int((stop - start) / step + 1))

# Basadas en Central Difference Method (Scarborough, 1966)
def derivada(f, x, deltaa_x):
    """
    Calcula la derivada de una función en un punto dado utilizando el método de diferencias centrales.

    Args:
        f (function): La función de la cual se desea calcular la derivada.
        x (float): El punto en el cual se desea calcular la derivada.
        deltaa_x (float): Un pequeño incremento en x para calcular la diferencia.

    Returns:
        float: La derivada de la función en el punto dado.
    """
    return (f(x + deltaa_x) - f(x - deltaa_x)) / (2 * deltaa_x)

def segunda_derivada(f, x, deltaa_x):
    """
    Calcula la segunda derivada de una función en un punto dado utilizando el método de diferencias centrales.

    Args:
        f (function): La función de la cual se desea calcular la segunda derivada.
        x (float): El punto en el cual se desea calcular la segunda derivada.
        deltaa_x (float): Un pequeño incremento en x para calcular la diferencia.

    Returns:
        float: La segunda derivada de la función en el punto dado.
    """
    return (f(x + deltaa_x) - 2 * f(x) + f(x - deltaa_x)) / (deltaa_x ** 2)

def delta_x(x):
    """
    Calcula un pequeño incremento basado en el valor absoluto de x.

    Args:
        x (float): El valor en el cual se basa el incremento.

    Returns:
        float: El pequeño incremento calculado.
    """
    if abs(x) > 0.01:
        return 0.01 * abs(x)
    else:
        return 0.0001

# Funciones 
def caja(l):
    """
    Calcula el volumen de una caja en función de la longitud de su lado.

    Args:
        l (float): La longitud del lado de la caja.

    Returns:
        float: El volumen de la caja.
    """
    return -1*(4*(l)**3 - 60*(l)**2 + 200*l)

def lata(r):
    """
    Calcula el área de superficie de una lata en función de su radio.

    Args:
        r (float): El radio de la lata.

    Returns:
        float: El área de superficie de la lata.
    """
    return 2 * np.pi * (r**2)  + 500/r

def f1(x):
    """
    Función matemática f1.

    Args:
        x (float): Variable independiente.

    Returns:
        float: Valor de la función f1.
    """
    return ((x)**2) + 54/x

def f2(x):
    """
    Función matemática f2.

    Args:
        x (float): Variable independiente.

    Returns:
        float: Valor de la función f2.
    """
    return ((x)**3) + (2*(x)) - 3

def f3(x):
    """
    Función matemática f3.

    Args:
        x (float): Variable independiente.

    Returns:
        float: Valor de la función f3.
    """
    return ((x)**4) + ((x)**2) - 33

def f4(x):
    """
    Función matemática f4.

    Args:
        x (float): Variable independiente.

    Returns:
        float: Valor de la función f4.
    """
    return (3*((x)**4)) - (8*((x)**3)) - (6*((x)**2)) + 12*(x)

# Arreglos con los límites generados para cada función
lim_lata = linspace(0.5, 8)
lim_caja = linspace(2, 3)
lim_f1 = linspace(0, 10)
lim_f2 = linspace(0, 5)
lim_f3 = linspace(-2.5, 2.5)
lim_f4 = linspace(-1.5, 3)

def biseccion(a, b, epsilon, f):
    """
    Encuentra una raíz de una función utilizando el método de bisección.

    Args:
        a (float): Límite inferior del intervalo.
        b (float): Límite superior del intervalo.
        epsilon (float): Precisión deseada.
        f (function): La función de la cual se desea encontrar la raíz.

    Returns:
        float: Aproximación de la raíz de la función.
    """
    x1, x2 = a, b
    z = (x1 + x2) / 2  
    while abs(derivada(f, z, delta_x(z) )) > epsilon: 
        z = (x1 + x2) / 2
        if derivada(f,z,delta_x(z)) < 0:  
            x1=z
        else:  
            x2 = z
    return z  

print(biseccion(0.6, 7, 0.5,f1))

# Calcular puntos para cada función
puntos_lata1 = biseccion(0.6, 5, 0.5, lata)
puntos_lata2 = biseccion(0.6, 5, 0.1, lata)
puntos_lata3 = biseccion(0.6, 5, 0.01, lata)
puntos_lata4 = biseccion(0.6, 5, 0.0001, lata)

puntos_caja1 = biseccion(2, 3, 0.5, caja)
puntos_caja2 = biseccion(2, 3, 0.1, caja)
puntos_caja3 = biseccion(2, 3, 0.01, caja)
puntos_caja4 = biseccion(2, 3, 0.0001, caja)

puntos_f11 = biseccion(0.6, 5, 0.5, f1)
puntos_f12 = biseccion(0.6, 5, 0.1, f1)
puntos_f13 = biseccion(0.6, 5, 0.01, f1)
puntos_f14 = biseccion(0.6, 5, 0.0001, f1)

'''
puntos_f21 = golden_search(0.6, 5, 0.5, f2)
puntos_f22 = golden_search(0.6, 5, 0.1, f2)
puntos_f23 = golden_search(0.6, 5, 0.01, f2)
puntos_f24 = golden_search(0.6, 5, 0.0001, f2)
'''

puntos_f31 = biseccion(-2, 2.5, 0.5, f3)
puntos_f32 = biseccion(-2, 2.5, 0.1, f3)
puntos_f33 = biseccion(-2, 2.5, 0.01, f3)
puntos_f34 = biseccion(-2, 2.5, 0.0001,f3)

puntos_f41 = biseccion(-1.8, 2.5, 0.5, f4)
puntos_f42 = biseccion(-1.8, 2.5, 0.1, f4)
puntos_f43 = biseccion(-1.8, 2.5, 0.01,f4)
puntos_f44 = biseccion(-1.8, 2.5, 0.0001,f4)

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