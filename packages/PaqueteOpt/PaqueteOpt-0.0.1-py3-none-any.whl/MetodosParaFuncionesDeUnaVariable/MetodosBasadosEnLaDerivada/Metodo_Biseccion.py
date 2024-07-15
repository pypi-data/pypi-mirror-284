import numpy as np
import matplotlib.pyplot as plt

def encontrar_raiz(a, b, epsilon, f):
    """
    Encuentra una raíz de la función f en el intervalo [a, b] utilizando el método de bisección.

    Args:
    - a: Extremo izquierdo del intervalo inicial.
    - b: Extremo derecho del intervalo inicial.
    - epsilon: Tolerancia para la precisión de la raíz.
    - f: Función objetivo cuya raíz se desea encontrar.

    Returns:
    - z: Aproximación de la raíz de la función f en el intervalo [a, b].
    """
    x1, x2 = a, b
    z = (x1 + x2) / 2  
    while abs(derivada(f, z, delta(z))) > epsilon: 
        z = (x1 + x2) / 2
        if derivada(f, z, delta(z)) < 0:  
            x1 = z
        else:  
            x2 = z
    return z  

def delta(x):
    if abs(x) > 0.01:
        return 0.01 * abs(x)
    else:
        return 0.0001

def derivada(f, x, delta_x):
    return (f(x + delta_x) - f(x - delta_x)) / (2 * delta_x)

def caja(l):
    return -1 * (4 * (l) ** 3 - 60 * (l) ** 2 + 200 * l)

def lata(r):
    return 2 * np.pi * (r ** 2)  + 500 / r

def f1(x):
    return ((x) ** 2) + 54 / x

def f2(x):
    return ((x) ** 3) + (2 * (x)) - 3

def f3(x):
    return ((x) ** 4) + ((x) ** 2) - 33

def f4(x):
    return (3 * ((x) ** 4)) - (8 * ((x) ** 3)) - (6 * ((x) ** 2)) + 12 * (x)

limite_lata = np.linspace(0.5, 8, 100)
limite_caja = np.linspace(2, 3, 100)
limite_f1 = np.linspace(0, 10, 100)
limite_f2 = np.linspace(0, 5, 100)
limite_f3 = np.linspace(-2.5, 2.5, 100)
limite_f4 = np.linspace(-1.5, 3, 100)

# Cálculo de puntos de raíces para cada función
puntos_lata1 = encontrar_raiz(0.6, 5, 0.5, lata)
puntos_lata2 = encontrar_raiz(0.6, 5, 0.1, lata)
puntos_lata3 = encontrar_raiz(0.6, 5, 0.01, lata)
puntos_lata4 = encontrar_raiz(0.6, 5, 0.0001, lata)

puntos_caja1 = encontrar_raiz(2, 3, 0.5, caja)
puntos_caja2 = encontrar_raiz(2, 3, 0.1, caja)
puntos_caja3 = encontrar_raiz(2, 3, 0.01, caja)
puntos_caja4 = encontrar_raiz(2, 3, 0.0001, caja)

puntos_f11 = encontrar_raiz(0.6, 5, 0.5, f1)
puntos_f12 = encontrar_raiz(0.6, 5, 0.1, f1)
puntos_f13 = encontrar_raiz(0.6, 5, 0.01, f1)
puntos_f14 = encontrar_raiz(0.6, 5, 0.0001, f1)

puntos_f31 = encontrar_raiz(-2, 2.5, 0.5, f3)
puntos_f32 = encontrar_raiz(-2, 2.5, 0.1, f3)
puntos_f33 = encontrar_raiz(-2, 2.5, 0.01, f3)
puntos_f34 = encontrar_raiz(-2, 2.5, 0.0001, f3)

puntos_f41 = encontrar_raiz(-1.8, 2.5, 0.5, f4)
puntos_f42 = encontrar_raiz(-1.8, 2.5, 0.1, f4)
puntos_f43 = encontrar_raiz(-1.8, 2.5, 0.01, f4)
puntos_f44 = encontrar_raiz(-1.8, 2.5, 0.0001, f4)
# Función lata

plt.figure(figsize=(8, 6))
plt.plot(limite_lata, lata(limite_lata), label='Función Lata')
plt.scatter(puntos_lata1, lata(puntos_lata1), label='Delta=0.5', marker='o')
plt.scatter(puntos_lata2, lata(puntos_lata2), label='Delta=0.1', marker='o')
plt.scatter(puntos_lata3, lata(puntos_lata3), label='Delta=0.01', marker='o')
plt.scatter(puntos_lata4, lata(puntos_lata4), label='Delta=0.0001', marker='o')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función Lata')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Función caja
plt.figure(figsize=(8, 6))
plt.plot(limite_caja, caja(limite_caja), label='Función Caja')
plt.scatter(puntos_caja1, caja(puntos_caja1), label='Delta=0.5', marker='o')
plt.scatter(puntos_caja2, caja(puntos_caja2), label='Delta=0.1', marker='o')
plt.scatter(puntos_caja3, caja(puntos_caja3), label='Delta=0.01', marker='o')
plt.scatter(puntos_caja4, caja(puntos_caja4), label='Delta=0.0001', marker='o')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función Caja')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Función f1
plt.figure(figsize=(8, 6))
plt.plot(limite_f1, f1(limite_f1), label='Función f1')
plt.scatter(puntos_f11, f1(puntos_f11), label='Delta=0.5', marker='o')
plt.scatter(puntos_f12, f1(puntos_f12), label='Delta=0.1', marker='o')
plt.scatter(puntos_f13, f1(puntos_f13), label='Delta=0.01', marker='o')
plt.scatter(puntos_f14, f1(puntos_f14), label='Delta=0.0001', marker='o')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función f1')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Función f3
plt.figure(figsize=(8, 6))
plt.plot(limite_f3, f3(limite_f3), label='Función f3')
plt.scatter(puntos_f31, f3(puntos_f31), label='Delta=0.5', marker='o')
plt.scatter(puntos_f32, f3(puntos_f32), label='Delta=0.1', marker='o')
plt.scatter(puntos_f33, f3(puntos_f33), label='Delta=0.01', marker='o')
plt.scatter(puntos_f34, f3(puntos_f34), label='Delta=0.0001', marker='o')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función f3')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Función f4
plt.figure(figsize=(8, 6))
plt.plot(limite_f4, f4(limite_f4), label='Función f4')
plt.scatter(puntos_f41, f4(puntos_f41), label='Delta=0.5', marker='o')
plt.scatter(puntos_f42, f4(puntos_f42), label='Delta=0.1', marker='o')
plt.scatter(puntos_f43, f4(puntos_f43), label='Delta=0.01', marker='o')
plt.scatter(puntos_f44, f4(puntos_f44), label='Delta=0.0001', marker='o')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función f4')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
