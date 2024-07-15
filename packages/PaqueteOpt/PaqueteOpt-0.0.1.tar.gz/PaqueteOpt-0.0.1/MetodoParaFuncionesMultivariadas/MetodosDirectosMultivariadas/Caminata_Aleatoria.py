import numpy as np

def random_walk(f, terminate_condition, x0, generate_step):
    """
    Realiza una búsqueda aleatoria iterativa para minimizar una función de costo f.

    Args:
    - f (función): Función de costo que se desea minimizar.
    - terminate_condition (función): Función de condición de terminación que evalúa si se debe detener la búsqueda.
    - x0 (array): Punto inicial para comenzar la búsqueda.
    - generate_step (función): Función que genera el siguiente paso en la búsqueda.

    Returns:
    - array: Mejor solución encontrada durante la búsqueda aleatoria.
    """
    x_best = x0
    x_current = x0

    while not terminate_condition(x_current):
        x_next = generate_step(x_current)
        if f(x_next) < f(x_best):
            x_best = x_next
        x_current = x_next
    
    return x_best

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

def termination_criteria(x, max_iter=100):
    termination_criteria.iterations += 1
    return termination_criteria.iterations >= max_iter

termination_criteria.iterations = 0  

def generate_random_step(x, mu=0, sigma=0.5):
    return x + np.random.normal(mu, sigma, size=len(x))

functions = [sphere_function, himmelblau_function, rastrigin_function, rosenbrock_function]
initial_points = [
    [5.0, 5.0],    
    [0.0, 0.0],    
    [5.12, 5.12],  
    [1.2, 1.2]     
]

best_solutions = []
for f, x0 in zip(functions, initial_points):
    termination_criteria.iterations = 0
    best_solution = random_walk(f, termination_criteria, x0, generate_random_step)
    best_solutions.append(best_solution)

for i, best_solution in enumerate(best_solutions):
    print(f"Mejor solución encontrada para la función {functions[i].__name__}: {best_solution}")
