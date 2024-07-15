import numpy as np
import matplotlib.pyplot as plt

def calcular_area_superficie(r, h):
    """
    Calcula el área de la superficie de un cilindro.

    Parámetros:
    r (float or array-like): El radio del cilindro.
    h (float or array-like): La altura del cilindro.

    Retorna:
    float or array-like: El área de la superficie del cilindro, 
                         que es la suma del área de las dos bases 
                         (2 * pi * r^2) y el área lateral (2 * pi * r * h).
    """
    sc = 2 * np.pi * (r ** 2)
    sl = 2 * np.pi * r * h
    return sc + sl

r = np.linspace(0.5, 8, 100)
h = np.linspace(0.5, 8, 100)

r1, h2 = np.meshgrid(r, h)
S = calcular_area_superficie(r1, h2)

print(S)

plt.scatter(r1, h2, c=S)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(r1, h2, S, cmap='viridis')

plt.show()