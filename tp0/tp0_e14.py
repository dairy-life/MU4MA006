"""
MU4MA006 - Travaux pratiques 0
2023-2024  Sorbonne Universite

See the LICENSE.txt file for license information.

Contributor(s):
Damiano Lombardi, Ruiyang DAI

"""

import numpy as np

"""
Exercice 14

Construire la matrice de taille $9 \times 9$ dont tous les \'el\'ements sont 
nuls sauf les \'el\'ements du 'bord' $i\in\{1,9\}$ ou $j\in\{1,9\}$, 
et les \'el\'ements du 'centre' $(i,j) \in \{4,5,6\} \times \{4,5,6\}$ qui valent $1$.

"""
print("\nExercice 14:")
print("Construct of matrix: \n")

# n: the dimension of the matrix M
# M: null matrix
n = 9
M = np.zeros((n, n))

# Set the first and last rows to 1
M[[0, -1], :] = 1

# Set the first and last columns to 1
M[:, [0, -1]] = 1

# Set the elements at indices vi,vi to 1 (center submatrix)
#vi = np.arange(3, 6)
#M[np.ix_(vi, vi)] = 1
M[np.ix_([3,4,5], [3,4,5])] = 1

print("Matrix M:")
print(M)

