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
Exercice 8 [Solveur lin\'eaire].

On consid\`ere la matrice de Hilbert H_n = (h_{i,j})_{1<=i,j<=n}
de taille n \times n de terme g\'en\'eral,
$$
h_{i,j} = 1 / (i+j-1) pour 1 <= i,j <= n.
$$
Ecrire une fonction construisant la matrice H_n.
On note $e$ le vecteur de taille $n$ dont toutes les composants sont
\'egales \`a $1$ et $b = H_n e$.
R\'esoudre, \`a l'aide d'un solveur lin\'eaire, le syst\`eme
$H_n x = b$ (sans utiliser une routine d'inversion de matrice).
Tracer l'erreur relative entre la solution obtenue et la solution exacte
en fonction de $n$. Toujours en fonction de $n$, \'etudier le conditionnement
en norme $2$ de $H_n$.

Mots clefs: np.linalg.solve, np.linalg.cond (Python)
"""
print("\nExercice 8:")
print("Linear solver:")
print("Study the relative error (between the solution obtained and the exact solution) and the 2-norm conditioning of Hilbert matrix. \n")

def MatHilbert(n):
    # Hilbert matrix 

    # param n: the dimension of the Hilbert matrix
    # return H: n \times n Hilbert matrix (NumPy Array)
    H = np.zeros((n, n))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            H[i - 1, j - 1] = 1 / (i + j - 1)
    return H

def compute_errors_and_conditions(vectTest):
    # Compute the errors and the condition numbers

    # param vectTest: test vectors of matrix dimension
    # return verr, vcond: vector of errors and vector of condition numbers
    verr = []
    vcond = []

    for n in vectTest:
        Hn = MatHilbert(n)
        e = np.ones((n, 1))
        b = np.dot(Hn, e)
        x = np.linalg.solve(Hn, -b)
        verr.append( np.linalg.norm(x - e) / np.linalg.norm(e))
        vcond.append(np.linalg.cond(Hn))

    return verr, vcond

# Test vectors, vector of errors and vector of condition numbers
vectTest = [10, 25, 50, 100, 150]
verr, vcond = compute_errors_and_conditions(vectTest)

# Plot the error
plt.figure(0)
plt.title('erreur')
plt.plot(vectTest, verr)

# Plot the condition number
plt.figure(1)
plt.title('cond')
plt.plot(vectTest, vcond, marker='o')

plt.show()
#Remarque: les matrices de Hilbert sont horriblement mal conditionnees.
