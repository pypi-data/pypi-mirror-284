import numpy as np
import matplotlib.pyplot as plt

def funcion_caja(l):
    return -1 * (4 * l**3 - 60 * l**2 + 200 * l)

def funcion_lata(r):
    return 2 * np.pi * (r**2) + 500 / r

def funcion_f1(x):
    return x**2 + 54 / x

def funcion_f3(x):
    return x**4 + x**2 - 33

def funcion_f4(x):
    return 3 * x**4 - 8 * x**3 - 6 * x**2 + 12 * x

def derivada(f, x, delta):
    return (f(x + delta) - f(x - delta)) / (2 * delta)

def segunda_derivada(f, x, delta):
    return (f(x + delta) - 2 * f(x) + f(x - delta)) / (delta ** 2)

def delta(x):
    if abs(x) > 0.01:
        return 0.01 * abs(x)
    else:
        return 0.0001

# Generar arrays usando np.linspace
limites_lata = np.linspace(0.5, 8, 100)
limites_caja = np.linspace(2, 3, 100)
limites_f1 = np.linspace(0, 10, 100)
limites_f3 = np.linspace(-2.5, 2.5, 100)
limites_f4 = np.linspace(-1.5, 3, 100)

# Implementación del método de Newton-Raphson
def metodo_newton_raphson(guess_inicial, epsilon, funcion, derivada, segunda_derivada):
    """
    Implementación del método de Newton-Raphson para encontrar una raíz de la función dada.

    Args:
    - guess_inicial: Valor inicial de la suposición para la raíz.
    - epsilon: Tolerancia para la precisión de la raíz.
    - funcion: Función objetivo cuya raíz se desea encontrar.
    - derivada: Función para calcular la primera derivada de la función.
    - segunda_derivada: Función para calcular la segunda derivada de la función.

    Returns:
    - x: Aproximación de la raíz de la función dentro de la tolerancia especificada.
    """
    x = guess_inicial
    while abs(derivada(funcion, x, delta(x))) > epsilon:
        segunda_deriv = segunda_derivada(funcion, x, delta(x))
        if segunda_deriv == 0:
            return x
        x = x - derivada(funcion, x, delta(x)) / segunda_deriv
    return x

# Calcular puntos para cada función
puntos_lata1 = metodo_newton_raphson(0.6, 0.5, funcion_lata, derivada, segunda_derivada)
puntos_lata2 = metodo_newton_raphson(0.6, 0.1, funcion_lata, derivada, segunda_derivada)
puntos_lata3 = metodo_newton_raphson(0.6, 0.01, funcion_lata, derivada, segunda_derivada)
puntos_lata4 = metodo_newton_raphson(0.6, 0.0001, funcion_lata, derivada, segunda_derivada)

puntos_caja1 = metodo_newton_raphson(2, 0.5, funcion_caja, derivada, segunda_derivada)
puntos_caja2 = metodo_newton_raphson(2, 0.1, funcion_caja, derivada, segunda_derivada)
puntos_caja3 = metodo_newton_raphson(2, 0.01, funcion_caja, derivada, segunda_derivada)
puntos_caja4 = metodo_newton_raphson(2, 0.0001, funcion_caja, derivada, segunda_derivada)

puntos_f11 = metodo_newton_raphson(0.6, 0.5, funcion_f1, derivada, segunda_derivada)
puntos_f12 = metodo_newton_raphson(0.6, 0.1, funcion_f1, derivada, segunda_derivada)
puntos_f13 = metodo_newton_raphson(0.6, 0.01, funcion_f1, derivada, segunda_derivada)
puntos_f14 = metodo_newton_raphson(0.6, 0.0001, funcion_f1, derivada, segunda_derivada)

puntos_f31 = metodo_newton_raphson(-2, 0.5, funcion_f3, derivada, segunda_derivada)
puntos_f32 = metodo_newton_raphson(-2, 0.1, funcion_f3, derivada, segunda_derivada)
puntos_f33 = metodo_newton_raphson(-2, 0.01, funcion_f3, derivada, segunda_derivada)
puntos_f34 = metodo_newton_raphson(-2, 0.0001, funcion_f3, derivada, segunda_derivada)

puntos_f41 = metodo_newton_raphson(-1.8, 0.5, funcion_f4, derivada, segunda_derivada)
puntos_f42 = metodo_newton_raphson(-1.8, 0.1, funcion_f4, derivada, segunda_derivada)
puntos_f43 = metodo_newton_raphson(-1.8, 0.01, funcion_f4, derivada, segunda_derivada)
puntos_f44 = metodo_newton_raphson(-1.8, 0.0001, funcion_f4, derivada, segunda_derivada)


#función lata
plt.figure(figsize=(8, 6))
plt.plot(limites_lata, funcion_lata(limites_lata))
plt.scatter(puntos_lata1, funcion_lata(puntos_lata1))
plt.scatter(puntos_lata2, funcion_lata(puntos_lata2))
plt.scatter(puntos_lata3, funcion_lata(puntos_lata3))
plt.scatter(puntos_lata4, funcion_lata(puntos_lata4))
plt.title('Función Lata')
plt.legend()
plt.grid(True)
plt.show()

#función caja
plt.figure(figsize=(8, 6))
plt.plot(limites_caja, funcion_caja(limites_caja))
plt.scatter(puntos_caja1, funcion_caja(puntos_caja1))
plt.scatter(puntos_caja2, funcion_caja(puntos_caja2))
plt.scatter(puntos_caja3, funcion_caja(puntos_caja3))
plt.scatter(puntos_caja4, funcion_caja(puntos_caja4))
plt.title('Función Caja')
plt.legend()
plt.grid(True)
plt.show()

#función f1
plt.figure(figsize=(8, 6))
plt.plot(limites_f1, funcion_f1(limites_f1))
plt.scatter(puntos_f11, funcion_f1(puntos_f11))
plt.scatter(puntos_f12, funcion_f1(puntos_f12))
plt.scatter(puntos_f13, funcion_f1(puntos_f13))
plt.scatter(puntos_f14, funcion_f1(puntos_f14))
plt.title('Función f1')
plt.legend()
plt.grid(True)
plt.show()

#función f3
plt.figure(figsize=(8, 6))
plt.plot(limites_f3, funcion_f3(limites_f3))
plt.scatter(puntos_f31, funcion_f3(puntos_f31))
plt.scatter(puntos_f32, funcion_f3(puntos_f32))
plt.scatter(puntos_f33, funcion_f3(puntos_f33))
plt.scatter(puntos_f34, funcion_f3(puntos_f34))
plt.title('Función f3')
plt.legend()
plt.grid(True)
plt.show()

#función f4
plt.figure(figsize=(8, 6))
plt.plot(limites_f4, funcion_f4(limites_f4))
plt.scatter(puntos_f41, funcion_f4(puntos_f41))
plt.scatter(puntos_f42, funcion_f4(puntos_f42))
plt.scatter(puntos_f43, funcion_f4(puntos_f43))
plt.scatter(puntos_f44, funcion_f4(puntos_f44))
plt.title('Función f4')
plt.legend()
plt.grid(True)
plt.show()
