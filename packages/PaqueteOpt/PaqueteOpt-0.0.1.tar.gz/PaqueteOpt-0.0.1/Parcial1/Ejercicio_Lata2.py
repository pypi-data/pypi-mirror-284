import matplotlib.pyplot as plt
import numpy as np

r = np.linspace(0.5, 8, 100)

def calcular_lata(r):
    """
    Calcula el área de la superficie de una lata cilíndrica con un volumen fijo.

    Parámetros:
    r (float or array-like): El radio de la lata.

    Retorna:
    float or array-like: El área de la superficie de la lata, 
                         que es la suma del área de las dos bases 
                         (2 * pi * r^2) y el área lateral 
                         para un volumen fijo de 500 unidades cúbicas.
    """
    s = (2 * np.pi * r ** 2) + (500 / r)
    return s

Sr = (500 / (4 * np.pi)) ** (1 / 3)

vH = 250 / (np.pi * Sr ** 2)
print(vH)

s_values = calcular_lata(r)

plt.plot(r, s_values)
plt.show()
