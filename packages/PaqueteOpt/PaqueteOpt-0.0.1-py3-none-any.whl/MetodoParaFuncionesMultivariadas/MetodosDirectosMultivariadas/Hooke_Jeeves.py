import numpy as np
import matplotlib.pyplot as plt

def hooke_jeeves(f, x0, delta, alpha=2, epsilon=1e-6, max_iter=1000):
    """
    Implementación del método de Hooke-Jeeves para la optimización no restringida.

    Args:
    - f: Función objetivo que se desea minimizar.
    - x0: Punto inicial de la búsqueda.
    - delta: Tamaño inicial del paso.
    - alpha: Factor de ampliación para explorar más en la dirección favorable (por defecto es 2).
    - epsilon: Tolerancia para el tamaño del paso (por defecto es 1e-6).
    - max_iter: Número máximo de iteraciones permitidas (por defecto es 1000).

    Returns:
    - x_best: Mejor punto encontrado que minimiza la función f.
    - f_best: Valor de la función objetivo en x_best.
    """
    def exploratory_move(x, delta):
        """
        Realiza un movimiento exploratorio a partir de un punto x dado un tamaño de paso delta.

        Args:
        - x: Punto actual desde el cual se realiza el movimiento exploratorio.
        - delta: Tamaño del paso para la exploración.

        Returns:
        - x_new: Nuevo punto después del movimiento exploratorio que minimiza la función f.
        """
        x_new = np.copy(x)
        f_current = f(x_new)
        for i in range(len(x)):
            x_new[i] += delta
            f_plus = f(x_new)
            if f_plus < f_current:
                f_current = f_plus
            else:
                x_new[i] -= 2 * delta
                f_temp = f(x_new)
                if f_temp < f_current:
                    f_current = f_temp
                else:
                    x_new[i] += delta
        return x_new
    
    x_base = np.array(x0)
    x_best = np.copy(x_base)
    f_best = f(x_best)
    
    for _ in range(max_iter):
        x_new = exploratory_move(np.copy(x_base), delta)
        f_new = f(x_new)
        
        if f_new < f_best:
            while f_new < f_best:
                x_base = np.copy(x_new)
                f_best = f_new
                x_new = x_base + alpha * (x_base - x_best)
                x_new = exploratory_move(np.copy(x_new), delta)
                f_new = f(x_new)
            x_best = np.copy(x_base)
        else:
            delta *= 0.5
            if delta < epsilon:
                break
    
    return x_best, f_best

def sphere_function(x):
    x = np.array(x)
    return np.sum(x**2)

def himmelblau_function(x):
    x = np.array(x)
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

def rastrigin_function(x):
    x = np.array(x)
    A = 10
    return A * len(x) + np.sum(x**2 - A * np.cos(2 * np.pi * x))

def rosenbrock_function(x):
    x = np.array(x)
    return np.sum(100 * (x[1:] - x[:-1]**2)**2 + (x[:-1] - 1)**2)

functions = [sphere_function, himmelblau_function, rastrigin_function, rosenbrock_function]
initial_points = [
    [5.0, 5.0],  
    [0.0, 0.0],  
    [5.12, 5.12],  
    [1.2, 1.2]   
]
delta = 0.5

for f, x0 in zip(functions, initial_points):
    x_best, f_best = hooke_jeeves(f, x0, delta)

    x = np.linspace(-5, 5, 400)
    y = np.linspace(-5, 5, 400)
    X, Y = np.meshgrid(x, y)
    Z = np.array([f([x, y]) for x, y in zip(np.ravel(X), np.ravel(Y))]).reshape(X.shape)
    
    plt.figure(figsize=(7, 6))
    cp = plt.contourf(X, Y, Z, levels=50, cmap='viridis')
    plt.colorbar(cp)
    plt.scatter(x_best[0], x_best[1], color='red', label='Optimal Point')
    plt.title(f'{f.__name__} Optimization Result\nBest Point: {x_best}, Best Value: {f_best:.4f}')
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.legend()
    plt.show()
