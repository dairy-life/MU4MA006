"""
MU4MA006 - Travaux pratiques 0
2023-2024  Sorbonne Universite

See the LICENSE.txt file for license information.

Contributor(s):
Damiano Lombardi, Ruiyang DAI

"""

import numpy as np

"""
Exercice 4 [Matrices particulières].

Trouver et tester les routines qui permettent de construire une matrice dont
tous les \'el\'ements sont nuls, une matrice dont tous les \'el\'ements sont
\'egaux \`a 1, la matrice identit\'e, et enfin de construire une matrice diagonale.

Mots clefs: np.zeros, np.ones, np.eye, np.diag (Python)
"""
print("Exercie 4:")
print("Construire des matrices via numpy:")

# Dimension of matrices
n = 5

# Create a matrix of zeros
zeros_matrix = np.zeros((n, n))
# Create a matrix of ones
ones_matrix  = np.ones((n, n))
# Create an identity matrix
identity_matrix  = np.eye(n)
# Create a diagonal matrix
vector = np.arange(1, n + 1)
diagonal_matrix = np.diag(vector)

print("Zeros Matrix:")
print(zeros_matrix)

print("\nOnes Matrix:")
print(ones_matrix)

print("\nIdentity Matrix:")
print(identity_matrix)

print("\nDiagonal Matrix:")
print(diagonal_matrix)
