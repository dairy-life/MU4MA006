"""
MU4MA006 - Travaux pratiques 0
2023-2024  Sorbonne Universite

See the LICENSE.txt file for license information.

Contributor(s):
Damiano Lombardi, Ruiyang DAI

"""

import numpy as np

"""
Exercice 12

Ecrire (puis tester) une fonction qui remplace les coefficients $A_{i,j}$ 
strictement positif d'une matrice $A$ par $0$ et laisse inchang\'es les autres.

"""
print("\nExercice 12: \n")

# Programmation 1
def tronque_size(A):
    n, m = A.shape
    for i in range(n):
        for j in range(m):
            if A[i, j] > 0:
                A[i, j] = 0
    return A

M = np.array([[1, 3, 2], [-5, 5, 1], [-10, 0, 3], [1, 1, -2]])
M = tronque_size(M)

print("Modified Matrix M:")
print("A function which replaces the strictly positive coefficients A_{i,j} of a matrix A by 0 and leaves the others unchanged: \n")

# Programmation 2 
def tronque_length(A):
    A[A > 0] = 0
    return A

M = np.array([[1, 3, 2], [-5, 5, 1], [-10, 0, 3], [1, 1, -2]])
M = tronque_length(M)

print("Modified Array M:")
print(M)

# Programmation 3 
def tronque(A):
    u = np.where(A > 0)
    A[u] = 0
    return A

M = np.array([[1, 3, 2], [-5, 5, 1], [-10, 0, 3], [1, 1, -2]])
M = tronque(M)

print("Modified Matrix M:")
print(M)

# Programmation 4 
M = np.array([[1, 3, 2], [-5, 5, 1], [-10, 0, 3], [1, 1, -2]])
M = np.minimum(M, 0)

print("Modified Matrix M:")
print(M)
