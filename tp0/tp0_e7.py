"""
MU4MA006 - Travaux pratiques 0
2023-2024  Sorbonne Universite

See the LICENSE.txt file for license information.

Contributor(s):
Damiano Lombardi, Ruiyang DAI

"""

import scipy.optimize as opt

"""
Exercice 7 [Z\'ero d'une fonction].

On s'int\'eresse ici \`a une approximation du nombre d'or, \phi = (1+\sqrt(5))/2.
On rappelle que \phi est l'unique solution positive de l'\'equation x^2-x-1=0.

1. D\'efinir la fonction f(x)=x^2-x-1.
2. Utiliser un solveur d'\'equation pour estimer \phi \`a partir de la r\'esolution de f(x)=0.


Mots clefs: from scipy.optimize import fsolve (Python)

Installation: pip install scipy
"""
print("\nExercice 7:")
print("Zero of Fibonacci function: \n")

def fFibo(x):
    # Function Fibonacci
    return x**2 - x - 1

# Find the roots of a function.
# Return the roots of the (non-linear) equations defined by func(x) = 0 
# given a starting estimate.
x0 = opt.fsolve(fFibo, -1)

print("Solution for x:", x0)
# Comments:
# In the line of code x0 = opt.fsolve(fFibo, 1),
# the 1 represents the initial guess for the root of the equation fFibo(x) = 0.
# 
# When using numerical root-finding algorithms like fsolve,
# you typically need to provide an initial estimate (or guess) for the root
# because these algorithms iteratively converge to the root starting from an initial point.
# The choice of the initial guess can affect
# whether the algorithm converges to the desired root or not.
# 
# In this case, 1 is the initial guess for the root of the equation.
# It means that the algorithm will start its search for the root from the point x = 1.
# Depending on the specific equation and problem,
# you might need to experiment with different initial guesses
# to ensure that the algorithm converges to the desired solution.
# 
# If you choose an initial guess that is relatively close to the actual root,
# the algorithm is more likely to converge quickly.
# If you choose a poor initial guess,
# the algorithm might require more iterations to converge,
# or it might even fail to converge to the correct root.
