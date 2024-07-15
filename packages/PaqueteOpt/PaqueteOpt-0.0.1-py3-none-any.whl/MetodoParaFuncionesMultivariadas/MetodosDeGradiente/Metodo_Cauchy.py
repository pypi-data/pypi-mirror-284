import numpy as np
import math

def regla_eliminacion(x1, x2, fx1, fx2, a, b):
    if fx1 > fx2:
        return x1, b

    if fx1 < fx2:
        return a, x2
    
    return x1, x2

def w_to_x(w, a, b):
    return w * (b - a) + a

def busquedaDorada(funcion, epsilon, a=None, b=None):
    PHI = (1 + math.sqrt(5)) / 2 - 1
    aw, bw = 0, 1
    Lw = 1
    k = 1

    while Lw > epsilon:
        w2 = aw + PHI * Lw
        w1 = bw - PHI * Lw
        aw, bw = regla_eliminacion(w1, w2, funcion(w_to_x(w1, a, b)), 
                                    funcion(w_to_x(w2, a, b)), aw, bw)
        k += 1
        Lw = bw - aw

    return (w_to_x(aw, a, b) + w_to_x(bw, a, b)) / 2

def gradiente(f, x, deltaX=0.001):
    grad = []
    for i in range(len(x)):
        xp = x.copy()
        xn = x.copy()
        xp[i] = xp[i] + deltaX
        xn[i] = xn[i] - deltaX
        grad.append((f(xp) - f(xn)) / (2 * deltaX))
    return np.array(grad)

def cauchy(funcion, x0, epsilon1, epsilon2, M):
    """
    Optimiza una función no lineal usando el método del gradiente descendente con línea de búsqueda.

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
        
        if np.linalg.norm(grad) < epsilon1 or k >= M:
            break
        
        def alpha_funcion(alpha):
            return funcion(xk - alpha * grad)
        
        alpha = busquedaDorada(alpha_funcion, epsilon=epsilon2, a=0.0, b=1.0)
        x_k1 = xk - alpha * grad
        
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

resultado = cauchy(himmenblau, x0, epsilon1, epsilon2, M)
print("Mejor solución encontrada:", resultado)
