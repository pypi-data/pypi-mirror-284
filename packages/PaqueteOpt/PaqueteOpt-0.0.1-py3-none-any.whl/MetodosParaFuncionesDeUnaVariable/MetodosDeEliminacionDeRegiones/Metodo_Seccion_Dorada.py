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

def busqueda_seccion_dorada(a, b, precision, f):
    """
    Realiza la búsqueda del mínimo de la función f en el intervalo [a, b] usando el método de la sección dorada.
    
    Parámetros:
    a, b : float
        Límites del intervalo inicial donde se busca el mínimo.
    precision : float
        Precisión deseada para la aproximación del mínimo.
    f : function
        Función objetivo que se desea minimizar.
        
    Retorna:
    float
        Aproximación del punto donde se encuentra el mínimo de la función f en el intervalo [a, b].
    """
    gr = (np.sqrt(5) + 1) / 2
    c = b - (b - a) / gr
    d = a + (b - a) / gr
    
    while abs(b - a) > precision:
        if f(c) < f(d):
            b = d
        else:
            a = c
        c = b - (b - a) / gr
        d = a + (b - a) / gr
    
    return (b + a) / 2

limites_lata = np.linspace(0.5, 8, 100)
limites_caja = np.linspace(2, 3, 100)
limites_f1 = np.linspace(0, 10, 100)
limites_f2 = np.linspace(0, 5, 100)
limites_f3 = np.linspace(-2.5, 2.5, 100)
limites_f4 = np.linspace(-1.5, 3, 100)

punto_lata1 = busqueda_seccion_dorada(0.6, 5, 0.5, lata)
punto_lata2 = busqueda_seccion_dorada(0.6, 5, 0.1, lata)
punto_lata3 = busqueda_seccion_dorada(0.6, 5, 0.01, lata)
punto_lata4 = busqueda_seccion_dorada(0.6, 5, 0.0001, lata)

punto_caja1 = busqueda_seccion_dorada(2, 3, 0.5, caja)
punto_caja2 = busqueda_seccion_dorada(2, 3, 0.1, caja)
punto_caja3 = busqueda_seccion_dorada(2, 3, 0.01, caja)
punto_caja4 = busqueda_seccion_dorada(2, 3, 0.0001, caja)

punto_f11 = busqueda_seccion_dorada(0.6, 5, 0.5, f1)
punto_f12 = busqueda_seccion_dorada(0.6, 5, 0.1, f1)
punto_f13 = busqueda_seccion_dorada(0.6, 5, 0.01, f1)
punto_f14 = busqueda_seccion_dorada(0.6, 5, 0.0001, f1)

punto_f21 = busqueda_seccion_dorada(0.6, 5, 0.5, f2)
punto_f22 = busqueda_seccion_dorada(0.6, 5, 0.1, f2)
punto_f23 = busqueda_seccion_dorada(0.6, 5, 0.01, f2)
punto_f24 = busqueda_seccion_dorada(0.6, 5, 0.0001, f2)

punto_f31 = busqueda_seccion_dorada(-2, 2.5, 0.5, f3)
punto_f32 = busqueda_seccion_dorada(-2, 2.5, 0.1, f3)
punto_f33 = busqueda_seccion_dorada(-2, 2.5, 0.01, f3)
punto_f34 = busqueda_seccion_dorada(-2, 2.5, 0.0001, f3)

punto_f41 = busqueda_seccion_dorada(-1.8, 2.5, 0.5, f4)
punto_f42 = busqueda_seccion_dorada(-1.8, 2.5, 0.1, f4)
punto_f43 = busqueda_seccion_dorada(-1.8, 2.5, 0.01, f4)
punto_f44 = busqueda_seccion_dorada(-1.8, 2.5, 0.0001, f4)

# Función lata
plt.figure(figsize=(8, 6))
plt.plot(limites_lata, lata(limites_lata), label='Función Lata')
plt.scatter([punto_lata1, punto_lata2, punto_lata3, punto_lata4], [lata(punto_lata1), lata(punto_lata2), lata(punto_lata3), lata(punto_lata4)])
plt.title('Función Lata')
plt.legend()
plt.grid(True)
plt.show()

# Función caja
plt.figure(figsize=(8, 6))
plt.plot(limites_caja, caja(limites_caja), label='Función Caja')
plt.scatter([punto_caja1, punto_caja2, punto_caja3, punto_caja4], [caja(punto_caja1), caja(punto_caja2), caja(punto_caja3), caja(punto_caja4)])
plt.title('Función Caja')
plt.legend()
plt.grid(True)
plt.show()

# Función f1
plt.figure(figsize=(8, 6))
plt.plot(limites_f1, f1(limites_f1), label='Función f1')
plt.scatter([punto_f11, punto_f12, punto_f13, punto_f14], [f1(punto_f11), f1(punto_f12), f1(punto_f13), f1(punto_f14)])
plt.title('Función f1')
plt.legend()
plt.grid(True)
plt.show()

# Función f2
plt.figure(figsize=(8, 6))
plt.plot(limites_f2, f2(limites_f2), label='Función f2')
plt.scatter([punto_f21, punto_f22, punto_f23, punto_f24], [f2(punto_f21), f2(punto_f22), f2(punto_f23), f2(punto_f24)])
plt.title('Función f2')
plt.legend()
plt.grid(True)
plt.show()

# Función f3
plt.figure(figsize=(8, 6))
plt.plot(limites_f3, f3(limites_f3), label='Función f3')
plt.scatter([punto_f31, punto_f32, punto_f33, punto_f34], [f3(punto_f31), f3(punto_f32), f3(punto_f33), f3(punto_f34)])
plt.title('Función f3')
plt.legend()
plt.grid(True)
plt.show()

# Función f4
plt.figure(figsize=(8, 6))
plt.plot(limites_f4, f4(limites_f4), label='Función f4')
plt.scatter([punto_f41, punto_f42, punto_f43, punto_f44], [f4(punto_f41), f4(punto_f42), f4(punto_f43), f4(punto_f44)])
plt.title('Función f4')
plt.legend()
plt.grid(True)
plt.show()
