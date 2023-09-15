"""
MU4MA006 - Travaux pratiques 1
2023-2024  Sorbonne Universite

See the LICENSE.txt file for license information.

Contributor(s):
Damiano Lombardi, Ruiyang DAI

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

"""
Travaux pratiques 1 [Schémas numériques pour un problème de Cauchy].

Étudier différents schémas pour approcher la solution d'un problème de Cauchy.

- implémenter un schéma numérique simple de type méthode d'Euler;
- comparer graphiquement la solution du schéma et celle du problème continu;
- réaliser une étude de convergence afin d'estimer l'ordre du schéma.

[Exercice 1] ODE

"""

# Constants 
T  =  1.0  # tps final
a  = -1.0  # parametre
u0 =  1.0  # cond init = uD

# fct edo
def f_exo1(t, u):
    # function F: [0, T] \times R^d --> R^d

    # param t: time   t_n (a variable)
    # param u: valeur u_n (a variable)
    # return : ODE        (a variable)
    return a * u
# Remarque:
#   Il faut bien trouver f_exo1 (la function F) que 
#   le problème (P_1) se reecrive sous la forme (P)

# sol anal
def sol1(t):
    # function: analytical solution: u_D * e^{a*t}

    # param t: time  t_n (NumPy Array) 
    # return : exact sol (NumPy Array)
    return u0 * np.exp(a * t)

# vect pr etude cv
vect_h = []        # le vecteur qui stocke le pas h (T/25, T/50, ...)
vect_Err_Eul = []  # le vecteur qui stocke l'erreur en norme infinie de la méthode d'Eul 
vect_Err_RK2 = []  # le vecteur qui stocke l'erreur en norme infinie de la méthode d'RK2
vect_Err_CN  = []  # le vecteur qui stocke l'erreur en norme infinie de la méthode d'CN

# boucle sur mesh pr etude cv
for N in [25, 50, 100, 200]:
    # gestion du temps
    h = T / N
    vect_h.append(h)
    vect_tn = np.arange(0, N + 1) * h

    # sol exacte
    uEx = sol1(vect_tn)

    # methode d’Euler
    uEul = np.ones(N + 1)
    # TODO:
    # Task: Please complete Euler methode here.
    err = np.max(np.abs(uEx - uEul))
    vect_Err_Eul.append(err)

    # methode RK2
    # TODO:
    # Task: Implement the Runge-Kutta 2nd Order (RK2) method to solve an ODE,
    # Step 1: Initialize the array uRK2 to store the computed solution
    # Step 2: Implement the RK2 method to calculate uRK2
    # Step 3: Calculate the maximum absolute error between uEx and uRK2

    # methode Crank-Nicolson
    # TODO:
    # Task: Implement the Crank-Nicolso (CN) method to solve an ODE,
    # Step 1: Initialize the array uCN to store the computed solution
    # Step 2: Implement the CN method to calculate uCN
    # Step 3: Calculate the maximum absolute error between uEx and uCN

    # on fait les plots pr petit cas
    if N == 25:
        # plot
        plt.figure(1)
        plt.plot(vect_tn, uEx,  label='Exact')
        plt.plot(vect_tn, uEul, label='Euler')
        plt.title('exo 1 - Euler')

        plt.figure(2)
        plt.plot(vect_tn, uEx,  label='Exact')
        plt.plot(vect_tn, uRK2, label='RK2')
        plt.title('exo 1 - RK2')

        plt.figure(3)
        plt.plot(vect_tn, uEx, label='Exact')
        plt.plot(vect_tn, uCN, label='CN')
        plt.title('exo 1 - CN')

# convergence: plot
plt.figure(4)
tabC = [6, 7, 2, 3, 5]
plt.plot(vect_h, vect_h, label='h')
plt.plot(vect_h, np.array(vect_h) ** 2, label='h^2')
plt.plot(vect_h, vect_Err_Eul, label='Euler')
plt.plot(vect_h, vect_Err_RK2, label='RK2')
plt.plot(vect_h, vect_Err_CN,  label='CN')
plt.legend(['h', 'h^2', 'Euler', 'RK2', 'CN'], loc='upper right')
plt.yscale('log')
plt.title('exo1 - cv')

plt.show()
