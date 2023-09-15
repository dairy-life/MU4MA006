"""
MU4MA006 - Travaux pratiques 0
2023-2024  Sorbonne Universite

See the LICENSE.txt file for license information.

Contributor(s):
Damiano Lombardi, Ruiyang DAI

"""

import numpy as np

"""
Exercice 10

On d\'efinit les vecteurs $u_1, u_2, u_3$ et $u_4$ de $R^5$ par

u1 = [1, -3,  3,  5 ,4],
u2 = [0,  1,  2,  4, 3],
u3 = [2, -5, -1, -6, 1],
u4 = [3,  4,  5, -2, 0].

Soit $A$ la matrice dont les colonnes sont form\'ees des vecteurs 
$u_1, \cdots, u_4$. Quel est le rang de A? 
M\^eme question si on remplace $u_4$ par le vecteur $[-3, 11, 4, 13, 4]$.
"""
print("\nExercice 10:")
print("The rank of a matrix: \n")

# Matrix A
u1 = np.array([1, -3,  3,  5, 4])
u2 = np.array([0,  1,  2,  4, 3])
u3 = np.array([2, -5, -1, -6, 1])
u4 = np.array([3,  4,  5, -2, 0])
A = np.column_stack((u1, u2, u3, u4))

# Rank of A
rank_A = np.linalg.matrix_rank(A)

print("Original Matrix A:")
print(A)
print("Rank of A:", rank_A)

# Modify the 4th column of A
A[:, 3] = [-3, 11, 4, 13, 4]

# Rank of A modified
rank_A_modified = np.linalg.matrix_rank(A)

print("\nModified Matrix A:")
print(A)
print("Rank of Modified A:", rank_A_modified)
