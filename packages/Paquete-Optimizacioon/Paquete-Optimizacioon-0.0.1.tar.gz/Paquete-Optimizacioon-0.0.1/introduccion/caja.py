import numpy as np
import matplotlib.pyplot as plt

def linspace(start, stop, step=1):
    """
    Genera números espaciados uniformemente en un intervalo especificado.

    Args:
        start (float): El inicio del intervalo.
        stop (float): El final del intervalo.
        step (float, optional): El paso entre números consecutivos en el intervalo. Por defecto es 1.

    Returns:
        np.ndarray: Un array de números espaciados uniformemente.
    """
    return np.linspace(start, stop, int((stop - start) / step + 1))

def volumen_caja(x):
    """
    Calcula el volumen de una caja con la fórmula V(x) = 200x - 60x^2 + 4x^3.

    Args:
        x (float): El valor de la variable independiente x.

    Returns:
        float: El volumen de la caja calculado usando la fórmula dada.
    """
    return 200 * x - 60 * x**2 + 4 * x**3

# Generar valores de x desde 2 hasta 3 con un paso de 0.05
x = linspace(2, 3, 0.05)

# Calcular el volumen de la caja para cada valor de x
v = volumen_caja(x)

# Valor específico de L
L = 2.11

# Calcular el volumen de la caja en el punto específico L
punto = volumen_caja(L)

# Graficar el volumen de la caja
plt.plot(x, v)
plt.scatter(L, punto, c='pink')
plt.xlabel('x')
plt.ylabel('Volumen')
plt.title('Volumen de la caja en función de x')
plt.show()
