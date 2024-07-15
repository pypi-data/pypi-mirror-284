import numpy as np
import matplotlib.pyplot as plt 

def linspace(start, stop, step=0.05):
    """
    Genera un arreglo espaciado uniformemente entre start y stop con el paso especificado.

    Args:
    - start (float): Valor inicial del arreglo.
    - stop (float): Valor final del arreglo.
    - step (float, opcional): Paso entre cada punto del arreglo. Por defecto es 0.05.

    Returns:
    - numpy.ndarray: Arreglo de valores espaciados uniformemente.
    """
    return np.linspace(start, stop, int((stop - start) / step + 1))

# Basadas en Central Difference Method (Scarborough, 1966)
def derivada(f, x, delta_x):
    """
    Calcula la derivada numérica de una función f en el punto x utilizando el método de diferencia central.

    Args:
    - f (function): Función para la cual se calcula la derivada.
    - x (float): Punto en el cual se evalúa la derivada.
    - delta_x (float): Incremento para calcular la derivada.

    Returns:
    - float: Valor de la derivada numérica en el punto x.
    """
    return (f(x + delta_x) - f(x - delta_x)) / (2 * delta_x)

def segunda_derivada(f, x, delta_x):
    """
    Calcula la segunda derivada numérica de una función f en el punto x utilizando el método de diferencia central.

    Args:
    - f (function): Función para la cual se calcula la segunda derivada.
    - x (float): Punto en el cual se evalúa la segunda derivada.
    - delta_x (float): Incremento para calcular la segunda derivada.

    Returns:
    - float: Valor de la segunda derivada numérica en el punto x.
    """
    return (f(x + delta_x) - 2 * f(x) + f(x - delta_x)) / (delta_x ** 2)

def delta_x(x):
    """
    Define el tamaño del paso delta_x basado en el valor absoluto de x.

    Args:
    - x (float): Valor para determinar el tamaño del paso delta_x.

    Returns:
    - float: Tamaño del paso delta_x.
    """
    if abs(x) > 0.01:
        return 0.01 * abs(x)
    else:
        return 0.0001

# Funciones específicas
def caja(l):
    """
    Función que calcula la función específica para la forma de una caja.

    Args:
    - l (float): Longitud específica para evaluar la función.

    Returns:
    - float: Valor calculado para la función caja en el punto l.
    """
    return -1*(4*(l)**3 - 60*(l)**2 + 200*l)

def lata(r):
    """
    Función que calcula la función específica para la forma de una lata.

    Args:
    - r (float): Radio específico para evaluar la función.

    Returns:
    - float: Valor calculado para la función lata en el punto r.
    """
    return 2 * np.pi * (r**2)  + 500/r

def f1(x):
    """
    Función matemática f1(x) = x^2 + 54/x.

    Args:
    - x (float): Valor de entrada para evaluar la función f1.

    Returns:
    - float: Valor calculado para la función f1 en el punto x.
    """
    return ((x)**2) + 54/x

def f2(x):
    """
    Función matemática f2(x) = x^3 + 2*x - 3.

    Args:
    - x (float): Valor de entrada para evaluar la función f2.

    Returns:
    - float: Valor calculado para la función f2 en el punto x.
    """
    return ((x)**3) + (2*(x)) - 3

def f3(x):
    """
    Función matemática f3(x) = x^4 + x^2 - 33.

    Args:
    - x (float): Valor de entrada para evaluar la función f3.

    Returns:
    - float: Valor calculado para la función f3 en el punto x.
    """
    return ((x)**4) + ((x)**2) - 33

def f4(x):
    """
    Función matemática f4(x) = 3*x^4 - 8*x^3 - 6*x^2 + 12*x.

    Args:
    - x (float): Valor de entrada para evaluar la función f4.

    Returns:
    - float: Valor calculado para la función f4 en el punto x.
    """
    return (3*((x)**4)) - (8*((x)**3)) - (6*((x)**2)) + 12*(x)

#Arreglos con los límites generados para cada función
lim_lata = linspace(0.5, 8)
lim_caja = linspace(2, 3)
lim_f1 = linspace(0, 10)
lim_f2 = linspace(0, 5)
lim_f3 = linspace(-2.5, 2.5)
lim_f4 = linspace(-1.5, 3)

def secante(a, b, epsilon, f):
    """
    Implementación del método de la secante para encontrar la raíz de una función f en el intervalo [a, b].

    Args:
    - a (float): Extremo izquierdo del intervalo inicial.
    - b (float): Extremo derecho del intervalo inicial.
    - epsilon (float): Tolerancia o precisión deseada para la raíz encontrada.
    - f (function): Función cuya raíz se busca.

    Returns:
    - float: Valor aproximado de la raíz de f en el intervalo [a, b].
    """

    x1, x2 = a, b
    z = x2 - (derivada(f, x2, delta_x(x2)) / (derivada(f, x2, delta_x(x2)) - derivada(f, x1, delta_x(x1)) / (x2 - x1)))
    while abs(derivada(f, z, delta_x(z))) > epsilon: 
        z = x2 - (derivada(f, x2, delta_x(x2)) / (derivada(f, x2, delta_x(x2)) - derivada(f, x1, delta_x(x1)) / (x2 - x1)))
        if derivada(f,z,delta_x(z)) < 0:  
            x1=z
        else:  
            x2 = z
    return z  

print(secante(0.6, 7, 0.5,f1))
print(secante(0.6, 7, 0.5,lata))

# Calcular puntos para cada función
puntos_lata1 = secante(0.6, 5, 0.5, lata)
puntos_lata2 = secante(0.6, 5, 0.1, lata)
puntos_lata3 = secante(0.6, 5, 0.01, lata)
puntos_lata4 = secante(0.6, 5, 0.0001, lata)

puntos_caja1 = secante(2, 3, 0.5, caja)
puntos_caja2 = secante(2, 3, 0.1, caja)
puntos_caja3 = secante(2, 3, 0.01, caja)
puntos_caja4 = secante(2, 3, 0.0001, caja)

puntos_f11 = secante(0.6, 5, 0.5, f1)
puntos_f12 = secante(0.6, 5, 0.1, f1)
puntos_f13 = secante(0.6, 5, 0.01, f1)
puntos_f14 = secante(0.6, 5, 0.0001, f1)

'''
puntos_f21 = golden_search(0.6, 5, 0.5, f2)
puntos_f22 = golden_search(0.6, 5, 0.1, f2)
puntos_f23 = golden_search(0.6, 5, 0.01, f2)
puntos_f24 = golden_search(0.6, 5, 0.0001, f2)
'''

puntos_f31 = secante(-2, 2.5, 0.5, f3)
puntos_f32 = secante(-2, 2.5, 0.1, f3)
puntos_f33 = secante(-2, 2.5, 0.01, f3)
puntos_f34 = secante(-2, 2.5, 0.0001,f3)

puntos_f41 = secante(-1.8, 2.5, 0.5, f4)
puntos_f42 = secante(-1.8, 2.5, 0.1, f4)
puntos_f43 = secante(-1.8, 2.5, 0.01,f4)
puntos_f44 = secante(-1.8, 2.5, 0.0001,f4)

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