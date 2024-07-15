import numpy as np

def gradiente(f, x, epsilon=1e-6):
    grad = np.zeros_like(x)
    for i in range(len(x)):
        x_plus = x.copy()
        x_minus = x.copy()
        x_plus[i] += epsilon
        x_minus[i] -= epsilon
        grad[i] = (f(x_plus) - f(x_minus)) / (2 * epsilon)
    return grad

def hessiano(f, x, epsilon=1e-6):
    n = len(x)
    hess = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                x_plus = x.copy()
                x_minus = x.copy()
                x_plus[i] += epsilon
                x_minus[i] -= epsilon
                hess[i, i] = (f(x_plus) - 2 * f(x) + f(x_minus)) / epsilon**2
            else:
                x_plus1 = x.copy()
                x_plus2 = x.copy()
                x_minus1 = x.copy()
                x_minus2 = x.copy()
                x_plus1[i] += epsilon
                x_plus1[j] += epsilon
                x_minus1[i] -= epsilon
                x_minus1[j] -= epsilon
                x_plus2[i] += epsilon
                x_minus2[j] -= epsilon
                hess[i, j] = (f(x_plus1) - f(x_minus1) - f(x_plus2) + f(x_minus2)) / (4 * epsilon**2)
    return hess

def newton(funcion, x0, epsilon1, epsilon2, M):
    """
    Optimiza una función no lineal usando el método de Newton.

    Parámetros:
    funcion (callable): La función objetivo a minimizar.
    x0 (array-like): Punto inicial para el algoritmo.
    epsilon1 (float): Tolerancia para el gradiente.
    epsilon2 (float): Tolerancia para el cambio relativo en x.
    M (int): Número máximo de iteraciones.

    Retorna:
    array-like: El punto encontrado que minimiza la función objetivo.
    """
    xk = x0
    k = 0
    while True:
        grad = gradiente(funcion, xk)
        hess = hessiano(funcion, xk)
        
        if np.linalg.norm(grad) < epsilon1 or k >= M:
            break
        
        dk = -np.linalg.inv(hess).dot(grad)
        alpha = 1.0
        x_k1 = xk + alpha * dk
        
        if np.linalg.norm(x_k1 - xk) / (np.linalg.norm(xk) + 0.00001) <= epsilon2:
            break
        
        k += 1
        xk = x_k1
    
    return xk

himmenblau = lambda x: (((x[0]**2) + x[1] - 11)**2) + ((x[0] + (x[1]**2) - 7)**2)

x0 = np.array([0.0, 0.0])
epsilon1 = 0.001
epsilon2 = 0.001
M = 100

resultado = newton(himmenblau, x0, epsilon1, epsilon2, M)
print("Mejor solución encontrada:", resultado)
