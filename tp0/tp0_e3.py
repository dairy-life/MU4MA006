"""
MU4MA006 - Travaux pratiques 0
2023-2024  Sorbonne Universite

See the LICENSE.txt file for license information.

Contributor(s):
Damiano Lombardi, Ruiyang DAI

"""

import numpy as np
import matplotlib.pyplot as plt

"""
Exercice 3 [Graphique simple].

Repr\'esenter la fonction sin(2 \pi x) sur [0,1].

Mots clefs: plt.plot (Python)

Installation: pip install matplotlib
"""
print("Exercie 3:")
print("Representer la fonction sin(2*pi*x) sur [0, 1].")
x = np.linspace(0, 1, 50)

def func_sin(x):
    # The function is designed to calculate the sine values.

    # param x: NumPy Array

    # comments: the compatible data types for the variable 'x'
    # can be NumPy Array, Float, List of Floats.
    # Clear comments leads to better use of the function.
    return np.sin(2.0 * np.pi * x)

# Call the function
y = func_sin(x)

# Plot
plt.plot(x, y)
plt.title('sin(2*pi*x)')
plt.show()
