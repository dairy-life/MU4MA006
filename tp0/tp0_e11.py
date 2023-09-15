"""
MU4MA006 - Travaux pratiques 0
2023-2024  Sorbonne Universite

See the LICENSE.txt file for license information.

Contributor(s):
Damiano Lombardi, Ruiyang DAI

"""

import numpy as np

"""
Exercice 11

Ecrire une fonction permettant de remplacer la $i$-\`eme ligne de la matrice A, 
not\'ee par $L_i$, par la ligne $\alpha L_j$, et la $j$-\`eme ligne par $L_i$. 
Si $i == j$, le fonction renvoie $A$ sans modification. 
Tester votre fonction sur des exemples de votre choix.
"""
print("\nExercice 11:")
print("Write a function to replace the i-th row of matrix A: \n")

def exo11(A, i, j, alpha):
    # function to replace the i-th row of matrix A

    # param A: matrix A (NumPy Array)
    # param i: i-th row of matrix A
    # param j: j-th col of matrix A
    # param alpha: scalar

    # return A: new matrix
    if i != j:
        aux = A[i - 1].copy()
        A[i - 1] = alpha * A[j - 1]
        A[j - 1] = aux
    return A

# Define matrix A
A = np.array([[ 1., -1.,  7.], 
              [-4.,  2., 11.], 
              [ 8.,  0.,  3.]])

print("Original Matrix A:")
print(A)

A = exo11(A, 1, 3, 0.5)
A = exo11(A, 2, 2, 0.5)

print("Modified Matrix A:")
print(A)
