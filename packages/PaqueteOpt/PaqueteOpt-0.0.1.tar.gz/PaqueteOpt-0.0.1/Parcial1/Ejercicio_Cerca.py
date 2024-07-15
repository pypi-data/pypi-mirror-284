import numpy as np
import matplotlib.pyplot as plt

def CalculoCerca(x):
    """
    Calcula el valor de la función 200*x - (8*x^2)/3.

    Parámetros:
    x (float or array-like): El valor o los valores en los cuales se evalúa la función.

    Retorna:
    float or array-like: El valor calculado de la función en los puntos x.
    """
    return 200 * x - (8 * (x ** 2) / 3)

x = np.linspace(-1, 4, 100)

v = CalculoCerca(x)
derivada = 200 - (16 / 3) * x

plt.plot(x, v)
plt.plot(x, derivada)
plt.legend()
plt.show()