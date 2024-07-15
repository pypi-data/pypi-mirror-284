import numpy as np

def nelder_mead(f, x0, gamma=2, beta=0.5, epsilon=1e-5, max_iter=1000):
    """
    Implementación del método de Nelder-Mead para la optimización no restringida.

    Args:
    - f: Función objetivo que se desea minimizar.
    - x0: Punto inicial de la búsqueda.
    - gamma: Parámetro de expansión para explorar más en una dirección favorable (por defecto es 2).
    - beta: Parámetro de contracción para ajustar el tamaño del simplex (por defecto es 0.5).
    - epsilon: Tolerancia para la convergencia (por defecto es 1e-5).
    - max_iter: Número máximo de iteraciones permitidas (por defecto es 1000).

    Returns:
    - x_best: Mejor punto encontrado que minimiza la función f.
    """
    N = len(x0)
    simplex = [np.array(x0)]
    for i in range(N):
        x = np.copy(x0)
        if x[i] != 0:
            x[i] = x[i] + (x[i] + 1)
        else:
            x[i] = 1
        simplex.append(x)
    simplex = np.array(simplex)

    for iteration in range(max_iter):
        simplex = sorted(simplex, key=lambda x: f(x))
        xh = simplex[-1]   
        xl = simplex[0]    
        xg = simplex[-2]   

        xc = np.mean(simplex[:-1], axis=0)

        xr = 2 * xc - xh
        if f(xr) < f(xl):
            xe = (1 + gamma) * xc - gamma * xh
            if f(xe) < f(xr):
                xnew = xe
            else:
                xnew = xr
        elif f(xr) < f(xg):
            xnew = xr
        else:
            if f(xr) < f(xh):
                xh = xr
            if f(xr) < f(xh):
                xc = xc - beta * (xc - xr)
            else:
                xc = xc - beta * (xc - xh)
            xnew = xc

        simplex[-1] = xnew

        f_values = np.array([f(x) for x in simplex])
        if np.sqrt(np.sum((f_values - np.mean(f_values)) ** 2) / (N + 1)) <= epsilon:
            break

    return simplex[0]


def sphere_function(x):
    return np.sum(x**2)

def himmelblau_function(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

def rastrigin_function(x):
    A = 10
    return A * len(x) + np.sum(x**2 - A * np.cos(2 * np.pi * x))

def rosenbrock_function(x):
    return np.sum(100 * (x[1:] - x[:-1]**2)**2 + (x[:-1] - 1)**2)

x0 = [-1.0, 1.5]
resultado_sphere = nelder_mead(sphere_function, x0)
print("Sphere function resultado:", resultado_sphere)

x0 = [0.0, 0.0]
resultado_himmelblau = nelder_mead(himmelblau_function, x0)
print("Himmelblau's function resultado:", resultado_himmelblau)

x0 = [-2.0, -2.0, -2.0]
resultado_rastrigin = nelder_mead(rastrigin_function, x0)
print("Rastrigin function resultado:", resultado_rastrigin)

x0 = [2.0, 1.5, 3.0, -1.5, -2.0]
resultado_rosenbrock = nelder_mead(rosenbrock_function, x0)
print("Rosenbrock function resultado:", resultado_rosenbrock)
