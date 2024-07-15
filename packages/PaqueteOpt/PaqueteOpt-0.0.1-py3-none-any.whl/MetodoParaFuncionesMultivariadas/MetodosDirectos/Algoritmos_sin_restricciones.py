import numpy as np
import matplotlib.pyplot as plt

def rastrigin(X):
    """
    Función de Rastrigin.
    
    Args:
        X (list or array): Lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: Valor de la función de Rastrigin en el punto (x, y).
    """
    A = 10
    return A * len(X) + sum([(x**2 - A * np.cos(2 * np.pi * x)) for x in X])

def ackley(X):
    """
    Función de Ackley.
    
    Args:
        X (list or array): Lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: Valor de la función de Ackley en el punto (x, y).
    """
    a = 20
    b = 0.2
    c = 2 * np.pi
    d = len(X)
    sum1 = sum([x**2 for x in X])
    sum2 = sum([np.cos(c * x) for x in X])
    term1 = -a * np.exp(-b * np.sqrt(sum1 / d))
    term2 = -np.exp(sum2 / d)
    return term1 + term2 + a + np.exp(1)

def esfera(X):
    """
    Función de Esfera.
    
    Args:
        X (list or array): Lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: Valor de la función de Esfera en el punto (x, y).
    """
    return sum([x**2 for x in X])

def rosenbrock(X):
    """
    Función de Rosenbrock.
    
    Args:
        X (list or array): Lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: Valor de la función de Rosenbrock en el punto (x, y).
    """
    return sum([100 * (X[i+1] - X[i]**2)**2 + (X[i] - 1)**2 for i in range(len(X)-1)])

def beale(X):
    """
    Función de Beale.
    
    Args:
        X (list or array): Lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: Valor de la función de Beale en el punto (x, y).
    """
    x, y = X
    return (1.5 - x + x*y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x*y**3)**2

def goldstein_price(X):
    """
    Función de Goldstein-Price.
    
    Args:
        X (list or array): Lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: Valor de la función de Goldstein-Price en el punto (x, y).
    """
    x, y = X
    return (1 + (x + y + 1)**2 * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2)) * \
           (30 + (2*x - 3*y)**2 * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2))

def cabina(X):
    """
    Función de la Cabina.
    
    Args:
        X (list or array): Lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: Valor de la función de la Cabina en el punto (x, y).
    """
    x, y = X
    return (x + 2*y - 7)**2 + (2*x + y - 5)**2

def bukin_n6(X):
    """
    Función de Bukin N. 6.
    
    Args:
        X (list or array): Lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: Valor de la función de Bukin N. 6 en el punto (x, y).
    """
    x, y = X
    return 100 * np.sqrt(np.abs(y - 0.01*x**2)) + 0.01 * np.abs(x + 10)

def matyas(X):
    """
    Función de Matyas.
    
    Args:
        X (list or array): Lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: Valor de la función de Matyas en el punto (x, y).
    """
    x, y = X
    return 0.26 * (x**2 + y**2) - 0.48 * x * y

def levi_n13(X):
    """
    Función de Levi N. 13.
    
    Args:
        X (list or array): Lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: Valor de la función de Levi N. 13 en el punto (x, y).
    """
    x, y = X
    return np.sin(3 * np.pi * x)**2 + (x - 1)**2 * (1 + np.sin(3 * np.pi * y)**2) + (y - 1)**2 * (1 + np.sin(2 * np.pi * y)**2)

def himmelblau(X):
    """
    Función de Himmelblau.
    
    Args:
        X (list or array): Lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: Valor de la función de Himmelblau en el punto (x, y).
    """
    x, y = X
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

def camello_tres_jorobas(X):
    """
    Función del Camello de Tres Jorobas.
    
    Args:
        X (list or array): Lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: Valor de la función del Camello de Tres Jorobas en el punto (x, y).
    """
    x, y = X
    return 2*x**2 - 1.05*x**4 + (x**6)/6 + x*y + y**2

def easom(X):
    """
    Función de Easom.
    
    Args:
        X (list or array): Lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: Valor de la función de Easom en el punto (x, y).
    """
    x, y = X
    return -np.cos(x) * np.cos(y) * np.exp(-((x - np.pi)**2 + (y - np.pi)**2))

def cruce_bandeja(X):
    """
    Función del Cruce de la Bandeja.
    
    Args:
        X (list or array): Lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: Valor de la función del Cruce de la Bandeja en el punto (x, y).
    """
    x, y = X
    return -0.0001 * (np.abs(np.sin(x) * np.sin(y) * np.exp(np.abs(100 - (np.sqrt(x**2 + y**2) / np.pi)))) + 1)**0.1

def portahuevos(X):
    """
    Función del Portahuevos.
    
    Args:
        X (list or array): Lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: Valor de la función del Portahuevos en el punto (x, y).
    """
    x, y = X
    return -(y + 47) * np.sin(np.sqrt(np.abs(x/2 + (y + 47)))) - x * np.sin(np.sqrt(np.abs(x - (y + 47))))

def holder(X):
    """
    Función de Holder Table.
    
    Args:
        X (list or array): Lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: Valor de la función de Holder Table en el punto (x, y).
    """
    x, y = X
    return -np.abs(np.sin(x) * np.cos(y) * np.exp(np.abs(1 - (np.sqrt(x**2 + y**2) / np.pi))))

def mccormick(X):
    """
    Función de McCormick.
    
    Args:
        X (list or array): Lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: Valor de la función de McCormick en el punto (x, y).
    """
    x, y = X
    return np.sin(x + y) + (x - y)**2 - 1.5*x + 2.5*y + 1

def schaffer_n2(X):
    """
    Función de Schaffer N. 2.
    
    Args:
        X (list or array): Lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: Valor de la función de Schaffer N. 2 en el punto (x, y).
    """
    x, y = X
    return 0.5 + (np.sin(x**2 - y**2)**2 - 0.5) / (1 + 0.001 * (x**2 + y**2))**2

def schaffer_n4(X):
    """
    Función de Schaffer N. 4.
    
    Args:
        X (list or array): Lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: Valor de la función de Schaffer N. 4 en el punto (x, y).
    """
    x, y = X
    return 0.5 + (np.cos(np.sin(np.abs(x**2 - y**2)))**2 - 0.5) / (1 + 0.001 * (x**2 + y**2))**2

def styblinski_tang(X):
    """
    Función de Styblinski-Tang.
    
    Args:
        X (list or array): Lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: Valor de la función de Styblinski-Tang en el punto (x, y).
    """
    return 0.5 * sum([x**4 - 16*x**2 + 5*x for x in X])

def shekel(X):
    """
    Función de Shekel.
    
    Args:
        X (list or array): Lista o arreglo con dos elementos representando las coordenadas x e y.
    
    Returns:
        float: Valor de la función de Shekel en el punto (x, y).
    """
    m = 10
    C = np.array([[4, 4],
                  [1, 1],
                  [8, 8],
                  [6, 6],
                  [3, 7],
                  [2, 9],
                  [5, 5],
                  [8, 1],
                  [6, 2],
                  [7, 3.6]])
    beta = np.array([0.1, 0.2, 0.2, 0.4, 0.4, 0.6, 0.3, 0.7, 0.5, 0.5])
    return -sum([1 / (np.sum((X - C[i])**2) + beta[i]) for i in range(m)])

limites_rastrigin = [(-5.12, 5.12), (-5.12, 5.12)]
limites_ackley = [(-5, 5), (-5, 5)]
limites_esfera = [(-5.12, 5.12), (-5.12, 5.12)]
limites_rosenbrock = [(-2, 2), (-2, 2)]
limites_beale = [(-4.5, 4.5), (-4.5, 4.5)]
limites_goldstein_price = [(-2, 2), (-2, 2)]
limites_cabina = [(-10, 10), (-10, 10)]
limites_bukin_n6 = [(-15, -5), (-3, 3)]
limites_matyas = [(-10, 10), (-10, 10)]
limites_levi_n13 = [(-10, 10), (-10, 10)]
limites_himmelblau = [(-5, 5), (-5, 5)]
limites_camello_tres_jorobas = [(-5, 5), (-5, 5)]
limites_easom = [(-100, 100), (-100, 100)]
limites_cruce_bandeja = [(-10, 10), (-10, 10)]
limites_portahuevos = [(-512, 512), (-512, 512)]
limites_holder = [(-10, 10), (-10, 10)]
limites_mccormick = [(-1.5, 4), (-3, 4)]
limites_schaffer_n2 = [(-100, 100), (-100, 100)]
limites_schaffer_n4 = [(-100, 100), (-100, 100)]
limites_styblinski_tang = [(-5, 5), (-5, 5)]
limites_shekel = [(0, 10), (0, 10)]

minimos_globales = {
    'rastrigin': [(0, 0)],
    'ackley': [(0, 0)],
    'esfera': [(0, 0)],
    'rosenbrock': [(0, 0)],
    'beale': [(3, 0.5)],
    'goldstein_price': [(0, -1)],
    'cabina': [(1, 3)],
    'bukin_n6': [(-10, 1)],
    'matyas': [(0, 0)],
    'levi_n13': [(1, 1)],
    'himmelblau': [(1, 1), (-0.84852813, -0.84852813), (-2.805118, 3.131312), (3.584428, -1.848126)],
    'camello_tres_jorobas': [(0, 0)],
    'easom': [(np.pi, np.pi)],
    'cruce_bandeja': [(0, 0)],
    'portahuevos': [(512, 404.2319)],
    'holder': [(0, 0)],
    'mccormick': [(-0.54719, -1.54719)],
    'schaffer_n2': [(0, 0)],
    'schaffer_n4': [(0, 0)],
    'styblinski_tang': [(0, 0)],
}

def plot_function(func, limites, minimos_globales, resolucion=100):
    x = np.linspace(limites[0][0], limites[0][1], resolucion)
    y = np.linspace(limites[1][0], limites[1][1], resolucion)
    X, Y = np.meshgrid(x, y)
    Z = np.array([[func([xi, yi]) for xi in x] for yi in y])

    plt.figure(figsize=(10, 8))
    cp = plt.contourf(X, Y, Z, 50, cmap='viridis')
    plt.colorbar(cp)
    plt.title(func.__name__)
    plt.xlabel('x')
    plt.ylabel('y')
    
    for minimo in minimos_globales.get(func.__name__, []):
        plt.plot(*minimo, 'r*', markersize=10)
    
    plt.show()

def plot_function_3d(func, limites, minimos_globales, resolucion=100):
    x = np.linspace(limites[0][0], limites[0][1], resolucion)
    y = np.linspace(limites[1][0], limites[1][1], resolucion)
    X, Y = np.meshgrid(x, y)
    Z = np.array([[func([xi, yi]) for xi in x] for yi in y])

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_title(func.__name__)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    
    for minimo in minimos_globales.get(func.__name__, []):
        ax.scatter(*minimo, func(minimo), color='red', s=100)
    
    plt.show()

plot_function(rastrigin, limites_rastrigin, minimos_globales)
plot_function(ackley, limites_ackley, minimos_globales)
plot_function(esfera, limites_esfera, minimos_globales)
plot_function(rosenbrock, limites_rosenbrock, minimos_globales)
plot_function(beale, limites_beale, minimos_globales)
plot_function(goldstein_price, limites_goldstein_price, minimos_globales)
plot_function(cabina, limites_cabina, minimos_globales)
plot_function(bukin_n6, limites_bukin_n6, minimos_globales)
plot_function(matyas, limites_matyas, minimos_globales)
plot_function(levi_n13, limites_levi_n13, minimos_globales)
plot_function(himmelblau, limites_himmelblau, minimos_globales)
plot_function(camello_tres_jorobas, limites_camello_tres_jorobas, minimos_globales)
plot_function(easom, limites_easom, minimos_globales)
plot_function(cruce_bandeja, limites_cruce_bandeja, minimos_globales)
plot_function(portahuevos, limites_portahuevos, minimos_globales)
plot_function(holder, limites_holder, minimos_globales)
plot_function(mccormick, limites_mccormick, minimos_globales)
plot_function(schaffer_n2, limites_schaffer_n2, minimos_globales)
plot_function(schaffer_n4, limites_schaffer_n4, minimos_globales)
plot_function(styblinski_tang, limites_styblinski_tang, minimos_globales)
plot_function_3d(shekel, limites_shekel, minimos_globales)
