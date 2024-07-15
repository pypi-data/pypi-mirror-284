import numpy as np
import math

def gradiente(f, x, epsilon=1e-5):
    N = len(x)
    grad = np.zeros(N)
    for i in range(N):
        xp = x.copy()
        xn = x.copy()
        xp[i] = xp[i] + epsilon
        xn[i] = xn[i] - epsilon
        grad[i] = (f(xp) - f(xn)) / (2 * epsilon)
    return grad

def regla_busqueda(x1, x2, fx1, fx2, a, b):
    if fx1 > fx2:
        return x1, b
    elif fx1 < fx2:
        return a, x2
    else:
        return x1, x2

def busqueda_linea(funcion, epsilon=1e-5, a=0.0, b=1.0):
    PHI = (1 + math.sqrt(5)) / 2 - 1
    aw, bw = 0, 1
    Lw = 1

    while Lw > epsilon:
        w2 = aw + PHI * Lw
        w1 = bw - PHI * Lw
        aw, bw = regla_busqueda(w1, w2, funcion(w1), funcion(w2), aw, bw)
        Lw = bw - aw

    return (aw + bw) / 2

def metodo_fletcher_reeves(funcion, x0, epsilon1, epsilon2, M):
    """
    Optimiza una función no lineal usando el método de Fletcher-Reeves (gradiente conjugado).

    Parámetros:
    funcion (callable): La función objetivo a minimizar.
    x0 (array-like): Punto inicial para el algoritmo.
    epsilon1 (float): Tolerancia para el gradiente.
    epsilon2 (float): Tolerancia para el cambio relativo en x.
    M (int): Número máximo de iteraciones.

    Retorna:
    array-like: El punto encontrado que minimiza la función objetivo.
    """
    terminar = False
    xk = x0
    k = 0
    s = -gradiente(funcion, xk)  

    while not terminar:
        if np.linalg.norm(s) < epsilon1 or k >= M:
            terminar = True
        else:
            def alpha_funcion(alpha):
                return funcion(xk + alpha * s)

            alpha = busqueda_linea(alpha_funcion, epsilon=epsilon2)
            x_k1 = xk + alpha * s

            grad_k = gradiente(funcion, xk)
            grad_k1 = gradiente(funcion, x_k1)
            beta = np.dot(grad_k1, grad_k1) / np.dot(grad_k, grad_k)
            s = -grad_k1 + beta * s

            if np.linalg.norm(x_k1 - xk) / (np.linalg.norm(xk) + 1e-8) <= epsilon2:
                terminar = True
            else:
                k += 1
                xk = x_k1

    return xk

himmenblau = lambda x: (((x[0]**2) + x[1] - 11)**2) + ((x[0] + (x[1]**2) - 7)**2)

x0 = np.array([1.0, 1.0])
epsilon1 = 0.001  
epsilon2 = 0.001  
M = 100  

solucion = metodo_fletcher_reeves(himmenblau, x0, epsilon1, epsilon2, M)
print("Solución encontrada:", solucion)
