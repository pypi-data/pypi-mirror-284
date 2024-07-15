import numpy as np
import matplotlib.pyplot as plt

def linspace(start, stop, step=1):
    """
    Genera una secuencia de números igualmente espaciados dentro de un intervalo definido.

    Parámetros:
    start (float): El valor inicial de la secuencia.
    stop (float): El valor final de la secuencia.
    step (float): El paso entre valores en la secuencia. Por defecto es 1.

    Retorna:
    np.ndarray: Un array de valores igualmente espaciados desde 'start' hasta 'stop', inclusivo.
    """
    return np.linspace(start, stop, int((stop - start) / step + 1))

def ecuacion_cerca(x):
    """
    Calcula el valor de la función 200x - (8/3)x^2.

    Parámetros:
    x (np.ndarray): Un array de valores de entrada.

    Retorna:
    np.ndarray: Un array de valores de salida calculados como 200x - (8/3)x^2.
    """
    return (200 * x) - (8 * (x)**2 / 3)

# Generar un conjunto de valores x desde -1 hasta 4 con un paso de 0.05
x = linspace(-1, 4, 0.05)

# Calcular los valores de la función ecuacion_cerca para los valores de x
v = ecuacion_cerca(x)

# Calcular la derivada de la función 200x - (8/3)x^2
derivada = 200 - ((16 / 3) * x)

# Graficar la función y su derivada
plt.plot(x, v, label='Ecuación')
plt.plot(x, derivada, c='pink', label='Derivada')

# Añadir leyenda y mostrar la gráfica
plt.legend()
plt.show()