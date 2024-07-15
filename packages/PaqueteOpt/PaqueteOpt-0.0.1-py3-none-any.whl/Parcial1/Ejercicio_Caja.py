import matplotlib.pyplot as plt
import numpy as np

def calcular_punto(L2):
    """
    Calcula el valor de la función 4*L2^3 - 60*L2^2 + 200*L2.

    Parámetros:
    L2 (float): El valor en el cual se evalúa la función.

    Retorna:
    float: El valor calculado de la función en el punto L2.
    """
    punto = (4 * (L2 ** 3)) - (60 * (L2 ** 2)) + (200 * L2)
    return punto

x = np.linspace(2, 3, 100)
v = (4 * (x ** 3)) - (60 * (x ** 2)) + (200 * x)

L2 = 2.11
punto = calcular_punto(L2)

plt.plot(x, v)
plt.scatter(L2, punto, color='red')
plt.legend()
plt.show()
