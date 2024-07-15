import numpy as np
import matplotlib.pyplot as plt

def caja(l):
    return -1 * (4 * (l)**3 - 60 * (l)**2 + 200 * l)

def lata(r):
    return 2 * np.pi * (r**2)  + 500 / r

def f1(x):
    return ((x)**2) + 54 / x

def f2(x):
    return ((x)**3) + (2 * (x)) - 3

def f3(x):
    return ((x)**4) + ((x)**2) - 33

def f4(x):
    return (3 * ((x)**4)) - (8 * ((x)**3)) - (6 * ((x)**2)) + 12 * (x)

limites_lata = np.linspace(0.5, 8, 100)
limites_caja = np.linspace(2, 3, 100)
limites_f1 = np.linspace(0, 10, 100)
limites_f2 = np.linspace(0, 5, 100)
limites_f3 = np.linspace(-2.5, 2.5, 100)
limites_f4 = np.linspace(-1.5, 3, 100)

def division_por_intervalos(x, delta, funcion):
    """
    Realiza una búsqueda del mínimo local de una función mediante el método de división por intervalos.

    Parámetros:
    x (float): Punto inicial para iniciar la búsqueda.
    delta (float): Tamaño del paso para expandir el intervalo de búsqueda.
    funcion (function): Función objetivo que se desea minimizar.

    Retorna:
    tuple: Un par de valores representando el intervalo [x1, x2] donde se estima que está el mínimo local.
    """
    k = 0
    if funcion(x - abs(delta)) >= funcion(x) >= funcion(x + abs(delta)):
        deltaa = delta
    elif funcion(x - abs(delta)) <= funcion(x) <= funcion(x + abs(delta)):
        deltaa = -delta
    x1 = x + (2**(k)) * deltaa
    x_anterior = x
    while funcion(x1) < funcion(x):
        k += 1
        x_anterior = x  
        x = x1
        x1 = x + (2 ** k) * deltaa
        
    return x_anterior, x1

puntos_lata1 = division_por_intervalos(0.6, 0.5, lata)
puntos_lata2 = division_por_intervalos(0.6, 0.1, lata)
puntos_lata3 = division_por_intervalos(0.6, 0.01, lata)
puntos_lata4 = division_por_intervalos(0.6, 0.0001, lata)

puntos_caja1 = division_por_intervalos(2.5, 0.5, caja)
puntos_caja2 = division_por_intervalos(2.5, 0.1, caja)
puntos_caja3 = division_por_intervalos(2.5, 0.01, caja)
puntos_caja4 = division_por_intervalos(2.5, 0.0001, caja)

puntos_f11 = division_por_intervalos(0.6, 0.5, f1)
puntos_f12 = division_por_intervalos(0.6, 0.1, f1)
puntos_f13 = division_por_intervalos(0.6, 0.01, f1)
puntos_f14 = division_por_intervalos(0.6, 0.0001, f1)

puntos_f31 = division_por_intervalos(-2, 0.5, f3)
puntos_f32 = division_por_intervalos(-2, 0.1, f3)
puntos_f33 = division_por_intervalos(-2, 0.01, f3)
puntos_f34 = division_por_intervalos(-2, 0.0001, f3)

puntos_f41 = division_por_intervalos(-1.5, 0.5, f4)
puntos_f42 = division_por_intervalos(-1.5, 0.1, f4)
puntos_f43 = division_por_intervalos(-1.5, 0.01, f4)
puntos_f44 = division_por_intervalos(-1.5, 0.0001, f4)

# Función Lata
plt.figure(figsize=(12, 8))
plt.plot(limites_lata, lata(limites_lata))
plt.scatter(puntos_lata1[0], lata(puntos_lata1[0]))
plt.scatter(puntos_lata2[0], lata(puntos_lata2[0]))
plt.scatter(puntos_lata3[0], lata(puntos_lata3[0]))
plt.scatter(puntos_lata4[0], lata(puntos_lata4[0]))
plt.title('Función Lata')
plt.legend()
plt.grid(True)
plt.show()

# Función Caja
plt.figure(figsize=(12, 8))
plt.plot(limites_caja, caja(limites_caja))
plt.scatter(puntos_caja1[0], caja(puntos_caja1[0]))
plt.scatter(puntos_caja2[0], caja(puntos_caja2[0]))
plt.scatter(puntos_caja3[0], caja(puntos_caja3[0]))
plt.scatter(puntos_caja4[0], caja(puntos_caja4[0]))
plt.title('Función Caja')
plt.legend()
plt.grid(True)
plt.show()

# Función f1
plt.figure(figsize=(12, 8))
plt.plot(limites_f1, f1(limites_f1))
plt.scatter(puntos_f11[1], f1(puntos_f11[1]))
plt.scatter(puntos_f12[1], f1(puntos_f12[1]))
plt.scatter(puntos_f13[1], f1(puntos_f13[1]))
plt.scatter(puntos_f14[1], f1(puntos_f14[1]))
plt.title('Función f1')
plt.legend()
plt.grid(True)
plt.show()

# Función f3
plt.figure(figsize=(12, 8))
plt.plot(limites_f3, f3(limites_f3))
plt.scatter(puntos_f31[1], f3(puntos_f31[1]))
plt.scatter(puntos_f32[1], f3(puntos_f32[1]))
plt.scatter(puntos_f33[0], f3(puntos_f33[0]))
plt.scatter(puntos_f34[1], f3(puntos_f34[1]))
plt.title('Función f3')
plt.legend()
plt.grid(True)
plt.show()

# Función f4
plt.figure(figsize=(12, 8))
plt.plot(limites_f4, f4(limites_f4))
plt.scatter(puntos_f41[1], f4(puntos_f41[1]))
plt.scatter(puntos_f42[1], f4(puntos_f42[1]))
plt.scatter(puntos_f43[1], f4(puntos_f43[1]))
plt.scatter(puntos_f44[1], f4(puntos_f44[1]))
plt.title('Función f4')
plt.legend()
plt.grid(True)
plt.show()
