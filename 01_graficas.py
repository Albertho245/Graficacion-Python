# -*- coding: utf-8 -*-
"""
Created on Tues Ago 29 2023

@author: AlbertoGallegos
"""

import matplotlib.pyplot as plt
import numpy as np

"Polinomio que nosotros elegimos"

plt.figure()
t = np.arange(-5, 5, 0.2)
plt.plot(t, t**3 - 4*t**2 + 2*t + 1, 'r--', label='P(x)')
plt.plot(t, (3*t**2 - 8*t + 2), 'bs', label="P'(x)")
plt.plot(t, (6*t - 8), 'go', label="P''(x)")

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polinomio y sus derivadas')
plt.grid(True)
plt.show()

"La graficacion del polinomio dado por el profe"

plt.figure()
n = 10
t = np.arange(0, n, 1)

acu1 = 1
acu2 = 0
factorials = []
squared_sums = []

for i in t:
    acu1 *= i
    acu2 += i**2
    factorials.append(acu1)
    squared_sums.append(acu2)

plt.plot(t, factorials, 'r--', label='Factoriales')
plt.plot(t, squared_sums, 'bs', label="Sumas de cuadrados")

plt.legend()
plt.xlabel('n')
plt.ylabel('Valor acumulado')
plt.title('y graficar el polinomio del siguiente código')
plt.grid(True)
plt.show()











