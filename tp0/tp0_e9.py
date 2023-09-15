"""
MU4MA006 - Travaux pratiques 0
2023-2024  Sorbonne Universite

See the LICENSE.txt file for license information.

Contributor(s):
Damiano Lombardi, Ruiyang DAI

"""

import numpy as np
from scipy.integrate import odeint 
import matplotlib.pyplot as plt

"""
Exercice 9 [R\'esolution d'un probl\`eme de Cauchy].

On consid\`ere ici le refroidissement d'une tasse de caf\'e fra\^ichement fait,
puis maintenu dans une pi\`ece \`a temp\'erature constante.
Aussi, l'\'evolution au cours du temps de la temp\'erature, not\'ee $T(t)$,
du caf\'e contenu dans cette tasse est d\'ecrite par,
$$
\left{
\begin{\aligned}
& T'(t) = 0.1 (T_A - T(t)),
& T (0) = T_{int},
\end{\aligned}
\right.
$$
o\`u $T_A$ la temp\'erature ambiante de la pi\`ece et $T_{ini}$ la temp\'erature
initiale du caf\'e. A l'aide d'un solveur pour \'equation diff\'erentielle ordinaire
avec donn\'ee intiale (dit probl\`eme de Cauchy), d\'eterminer puis tracer l'\'evolution
de T(t) sur l'intervalle de temps [0,60] avec $T_A = 20$ et $T_{ini} = 100$.
Qu'observez-vous ?

Mots clefs: from scipy.integrate import odeint (Python)
"""
print("\nExercice 9: \n")

# TA: la température ambiante de la pièce.
# Tini: la température initiale du café.
TA = 20
Tini = 100

def cafe(t, T):
    # ODE: 0.1 * (TA - T) 

    # param t: time space (NumPy Array)
    # param T: the evolution over time of the temperature (NumPy Array)
    # return ODE: 
    return 0.1 * (TA - T)

# Time span
t_space = np.linspace(0, 60, 100)

# Initial condition
initial_condition = [Tini]

# Solve the ODE using odeint
t_values = odeint(cafe, initial_condition, t_space)
# Comments:
# Solve a system of ordinary differential equations using 
# lsoda from the FORTRAN library odepack.
# Solves the initial value problem for stiff or non-stiff systems of first order ode-s:
# dy/dt = func(y, t, ...)
#
# Parameters of odeint(func, y0, t, ...):
# func: callable(y, t, ...)
#       computes the derivative of y at t;
# y0: array
#     inital condition on y
# t:  array
#     A sequence of time points for which to solve for y.

# Plot the results
plt.plot(t_space, t_values)
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Cafe Temperature Evolution')
plt.grid(True)
plt.show()
