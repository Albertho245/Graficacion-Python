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

n = 10 
cu1 = 1
acu2 = 0
cu1_accumulated = []
acu2_accumulated = []

for i in range(n):
    cu1 *= i
    acu2 += i**2
    cu1_accumulated.append(cu1)
    acu2_accumulated.append(acu2)

plt.figure()

t = np.arange(0, n, 1)
plt.plot(t, cu1_accumulated, 'r--', label='Acumulación cu1')
plt.plot(t, acu2_accumulated, 'bs', label="Acumulación acu2")

plt.legend()
plt.xlabel('n')
plt.ylabel('Valor acumulado')
plt.title('Graficacion del polinomio del profe')
plt.grid(True)
plt.show()











