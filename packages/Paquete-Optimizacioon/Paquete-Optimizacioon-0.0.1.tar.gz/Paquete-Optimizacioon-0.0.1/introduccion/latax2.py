import numpy as np
import matplotlib.pyplot as plt

def linspace(start, stop, step=1):
    """
    Genera números espaciados uniformemente en un intervalo especificado.

    Parámetros:
    - start (float): El valor inicial de la secuencia.
    - stop (float): El valor final de la secuencia.
    - step (float): El tamaño del paso entre los valores en la secuencia.

    Retorna:
    - numpy.ndarray: Una secuencia de valores espaciados uniformemente desde start hasta stop, inclusive.
    """
    return np.linspace(start, stop, int((stop - start) / step + 1))

def volumen_lata(r):
    """
    Calcula el volumen de una lata cilíndrica en función de su radio.

    Parámetros:
    - r (float): El radio de la base de la lata.

    Retorna:
    - float: El volumen de la lata.
    """
    return 2 * 3.1416 * (r**2) + 500 / r

# Generar valores de r y h
r = linspace(0.5, 8, 0.1)
h = linspace(0.5, 8, 0.1)

# Calcular la superficie lateral y la superficie total de la lata
sc = 2 * 3.1416 * (r**2)
sl = 2 * 3.1416 * r * h
S = 2 * 3.1416 * (r**2) + 500 / r

# Calcular la altura de la lata con un radio específico
h1 = 250 / (3.1416 * (3.414**2))
#print("H:", h1)

# Calcular el radio de la lata con un volumen específico (comentado)
# r1 = np.sqrt((500 / (4 * 3.1416)), 3)
#print(r1)

# Graficar la relación entre el radio y la superficie total
plt.plot(r, S)
plt.xlabel("Radio (r)")
plt.ylabel("Superficie Total (S)")
plt.title("Relación entre el Radio y la Superficie Total de una Lata")
plt.show()
