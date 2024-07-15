import numpy as np
import matplotlib.pyplot as plt

def caja(l):
    return -1 * (4 * l**3 - 60 * l**2 + 200 * l)

def lata(r):
    return 2 * np.pi * r**2 + 500 / r

def f1(x):
    return x**2 + 54 / x

def f2(x):
    return x**3 + 2 * x - 3

def f3(x):
    return x**4 + x**2 - 33

def f4(x):
    return 3 * x**4 - 8 * x**3 - 6 * x**2 + 12 * x

def generar_fibonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[-1] + fib[-2])
    return fib

def busqueda_fibonacci(a, b, n, precision, f):
    """
    Implementa el método de búsqueda por la secuencia de Fibonacci para encontrar el mínimo de una función en un intervalo dado.

    Parámetros:
    a (float): Extremo izquierdo del intervalo.
    b (float): Extremo derecho del intervalo.
    n (int): Número de términos de la secuencia de Fibonacci a utilizar.
    precision (float): Precisión deseada para la aproximación del mínimo.
    f (function): Función objetivo a minimizar.

    Retorna:
    float: Aproximación del punto donde se encuentra el mínimo de la función dentro del intervalo [a, b].
    """
    fib = generar_fibonacci(n)
    L = b - a
    x1 = a + (fib[n - 2] / fib[n]) * L
    x2 = a + (fib[n - 1] / fib[n]) * L

    f1_val = f(x1)
    f2_val = f(x2)
    
    for k in range(2, n):
        if abs(b - a) <= precision:
            break
        if f1_val > f2_val:
            a = x1
            x1 = x2
            x2 = a + (fib[n - k - 1] / fib[n - k]) * (b - a)
            f1_val = f2_val
            f2_val = f(x2)
        else:
            b = x2
            x2 = x1
            x1 = a + (fib[n - k - 2] / fib[n - k]) * (b - a)
            f2_val = f1_val
            f1_val = f(x1)
    
    return (a + b) / 2

limites_lata = np.linspace(0.5, 8, 100)
limites_caja = np.linspace(2, 3, 100)
limites_f1 = np.linspace(0, 10, 100)
limites_f2 = np.linspace(0, 5, 100)
limites_f3 = np.linspace(-2.5, 2.5, 100)
limites_f4 = np.linspace(-1.5, 3, 100)

punto_lata1 = busqueda_fibonacci(0.6, 5, 50, 0.5, lata)
punto_lata2 = busqueda_fibonacci(0.6, 5, 50, 0.1, lata)
punto_lata3 = busqueda_fibonacci(0.6, 5, 50, 0.01, lata)
punto_lata4 = busqueda_fibonacci(0.6, 5, 50, 0.0001, lata)

punto_caja1 = busqueda_fibonacci(2, 3, 50, 0.5, caja)
punto_caja2 = busqueda_fibonacci(2, 3, 50, 0.1, caja)
punto_caja3 = busqueda_fibonacci(2, 3, 50, 0.01, caja)
punto_caja4 = busqueda_fibonacci(2, 3, 50, 0.0001, caja)

punto_f11 = busqueda_fibonacci(0.6, 5, 50, 0.5, f1)
punto_f12 = busqueda_fibonacci(0.6, 5, 50, 0.1, f1)
punto_f13 = busqueda_fibonacci(0.6, 5, 50, 0.01, f1)
punto_f14 = busqueda_fibonacci(0.6, 5, 50, 0.0001, f1)

punto_f21 = busqueda_fibonacci(0.6, 5, 50, 0.5, f2)
punto_f22 = busqueda_fibonacci(0.6, 5, 50, 0.1, f2)
punto_f23 = busqueda_fibonacci(0.6, 5, 50, 0.01, f2)
punto_f24 = busqueda_fibonacci(0.6, 5, 50, 0.0001, f2)

punto_f31 = busqueda_fibonacci(-2, 2.5, 50, 0.5, f3)
punto_f32 = busqueda_fibonacci(-2, 2.5, 50, 0.1, f3)
punto_f33 = busqueda_fibonacci(-2, 2.5, 50, 0.01, f3)
punto_f34 = busqueda_fibonacci(-2, 2.5, 50, 0.0001, f3)

punto_f41 = busqueda_fibonacci(-1.8, 2.5, 50, 0.5, f4)
punto_f42 = busqueda_fibonacci(-1.8, 2.5, 50, 0.1, f4)
punto_f43 = busqueda_fibonacci(-1.8, 2.5, 50, 0.01, f4)
punto_f44 = busqueda_fibonacci(-1.8, 2.5, 50, 0.0001, f4)

#función lata
plt.figure(figsize=(15, 10))
plt.plot(limites_lata, lata(limites_lata), label='Función Lata')
plt.scatter([punto_lata1, punto_lata2, punto_lata3, punto_lata4], [lata(punto_lata1), lata(punto_lata2), lata(punto_lata3), lata(punto_lata4)], label='Puntos Lata', c='r')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función Lata')
plt.legend()
plt.grid(True)
plt.show()

#función caja
plt.plot(limites_caja, caja(limites_caja), label='Función Caja')
plt.scatter([punto_caja1, punto_caja2, punto_caja3, punto_caja4], [caja(punto_caja1), caja(punto_caja2), caja(punto_caja3), caja(punto_caja4)], label='Puntos Caja', c='r')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función Caja')
plt.legend()
plt.grid(True)
plt.show()

#función f1
plt.plot(limites_f1, f1(limites_f1), label='Función f1')
plt.scatter([punto_f11, punto_f12, punto_f13, punto_f14], [f1(punto_f11), f1(punto_f12), f1(punto_f13), f1(punto_f14)], label='Puntos f1', c='r')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función f1')
plt.legend()
plt.grid(True)
plt.show()

#función f2
plt.plot(limites_f2, f2(limites_f2), label='Función f2')
plt.scatter([punto_f21, punto_f22, punto_f23, punto_f24], [f2(punto_f21), f2(punto_f22), f2(punto_f23), f2(punto_f24)], label='Puntos f2', c='r')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función f2')
plt.legend()
plt.grid(True)
plt.show()

#función f3
plt.plot(limites_f3, f3(limites_f3), label='Función f3')
plt.scatter([punto_f31, punto_f32, punto_f33, punto_f34], [f3(punto_f31), f3(punto_f32), f3(punto_f33), f3(punto_f34)], label='Puntos f3', c='r')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función f3')
plt.legend()
plt.grid(True)
plt.show()

#función f4
plt.plot(limites_f4, f4(limites_f4), label='Función f4')
plt.scatter([punto_f41, punto_f42, punto_f43, punto_f44], [f4(punto_f41), f4(punto_f42), f4(punto_f43), f4(punto_f44)], label='Puntos f4', c='r')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función f4')
plt.legend()
plt.grid(True)
plt.show()
