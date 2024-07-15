import numpy as np
import matplotlib.pyplot as plt

def rosenbrock_cubica_linea(X):
    """
    Calcula el valor de la función de Rosenbrock cúbica en una línea dada.
    
    Args:
        X (list or array): Una lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: El valor de la función en el punto (x, y).
    """
    x, y = X
    return (1 - x)**2 + 100 * (y - x**2)**2 + (y - 1)**3 + (x + 1)**3

def rosenbrock_disco(X):
    """
    Calcula el valor de la función de Rosenbrock dentro de un disco de radio 2.
    
    Args:
        X (list or array): Una lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: El valor de la función en el punto (x, y) si está dentro del disco, de lo contrario None.
    """
    x, y = X
    if x**2 + y**2 <= 2:
        return (1 - x)**2 + 100 * (y - x**2)**2

def mishra_pajaro_restringida(X):
    """
    Calcula el valor de la función Mishra Bird dentro de una restricción circular.
    
    Args:
        X (list or array): Una lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: El valor de la función en el punto (x, y) si está dentro de la restricción, de lo contrario np.inf.
    """
    x, y = X
    if (x+5)**2 + (y+5)**2 < 25:
        return np.sin(y) * np.exp((1 - np.cos(x))**2) + np.cos(x) * np.exp((1 - np.sin(y))**2) + (x - y)**2

    return np.inf

def townsend(X):
    """
    Calcula el valor de la función de Townsend en un punto dado.
    
    Args:
        X (list or array): Una lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: El valor de la función en el punto (x, y).
    """
    x, y = X
    return (x - 1)**2 + (y - 1)**2 + np.exp(-x*y)

def gomez_levy(X):
    """
    Calcula el valor de la función de Gomez Levy en un punto dado.
    
    Args:
        X (list or array): Una lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: El valor de la función en el punto (x, y).
    """
    x, y = X
    return (x - 1)**2 + (y - 1)**2 - np.sin(4*np.pi*x) * np.sin(2*np.pi*y)

def simionescu(X):
    """
    Calcula el valor de la función de Simionescu en un punto dado.
    
    Args:
        X (list or array): Una lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: El valor de la función en el punto (x, y).
    """
    x, y = X
    return np.sin(x) * np.cos(y) + np.sin(y) * np.cos(x)

limites_rosenbrock_cubica_linea = [(-3, 3), (-3, 3)]
limites_rosenbrock_disco = [(-2, 2), (-2, 2)]
limites_mishra_pajaro_restringida = [(-4, 0), (-4, 0)]
limites_townsend = [(-2, 2), (-2, 2)]
limites_gomez_levy = [(-2, 2), (-2, 2)]
limites_simionescu = [(-2, 2), (-2, 2)]

min_rosenbrock_cubica_linea = (1.0, 1.0)
min_rosenbrock_disco = (1.0, 1.0)
min_mishra_pajaro_restringida = (-3.1302468, -1.5821422)
min_townsend = (2.0052938, 1.1944509)
min_gomez_levy = (0.08984201, -0.7126564)
min_simionescu = (0.84852813, -0.84852813)


def plot_function_with_global_minimum(func, bounds, global_minimum, resolution=100):
    x = np.linspace(bounds[0][0], bounds[0][1], resolution)
    y = np.linspace(bounds[1][0], bounds[1][1], resolution)
    X, Y = np.meshgrid(x, y)
    Z = np.array([[func([xi, yi]) for xi in x] for yi in y])

    plt.figure(figsize=(10, 8))
    cp = plt.contourf(X, Y, Z, 50, cmap='viridis')
    plt.colorbar(cp)
    plt.title(func.__name__)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter(global_minimum[0], global_minimum[1], color='red', marker='o', label='Global Minimum')
    plt.legend()
    plt.show()

plot_function_with_global_minimum(rosenbrock_cubica_linea, limites_rosenbrock_cubica_linea, min_rosenbrock_cubica_linea)
plot_function_with_global_minimum(rosenbrock_disco, limites_rosenbrock_disco, min_rosenbrock_disco)
plot_function_with_global_minimum(mishra_pajaro_restringida, limites_mishra_pajaro_restringida, min_mishra_pajaro_restringida)
plot_function_with_global_minimum(townsend, limites_townsend, min_townsend)
plot_function_with_global_minimum(gomez_levy, limites_gomez_levy, min_gomez_levy)
plot_function_with_global_minimum(simionescu, limites_simionescu, min_simionescu)
