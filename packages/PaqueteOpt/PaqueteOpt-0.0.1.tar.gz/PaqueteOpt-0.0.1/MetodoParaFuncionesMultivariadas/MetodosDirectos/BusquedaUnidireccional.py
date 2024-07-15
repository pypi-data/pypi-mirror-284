import numpy as np
import matplotlib.pyplot as plt


xt = np.array([2, 2])
xs = np.array([1, 5])
alpha = 0.1

def objective_function(x1, x2):
    """
    Función objetivo: suma de cuadrados de las diferencias con el punto óptimo (10, 10)
    """
    return (x1 - 10) ** 2 + (x2 - 10) ** 2

def next_point(xt, xs, alpha):
    """
    Calcula el próximo punto en la dirección de búsqueda.

    Args:
    - xt (np.array): Punto actual.
    - xs (np.array): Dirección de búsqueda.
    - alpha (float): Tamaño del paso.

    Returns:
    - np.array: Nuevo punto calculado.
    """
    return xt + alpha * xs


xa = next_point(xt, xs, alpha)
x1, x2 = xa[0], xa[1]
result = objective_function(x1, x2)


print("Nuevo punto:", xa)
print("Valor de la función objetivo en el nuevo punto:", result)
plt.plot(xt[0], xt[1], 'bo', label='Punto inicial')
plt.plot(xa[0], xa[1], 'ro', label='Nuevo punto')
plt.arrow(xt[0], xt[1], alpha * xs[0], alpha * xs[1], head_width=0.1, head_length=0.1, fc='g', ec='g', label='Dirección de búsqueda')
plt.title('Búsqueda Unidireccional')
plt.grid(True)
plt.show()
