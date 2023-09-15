"""
MU4MA006 - Travaux pratiques 0
2023-2024  Sorbonne Universite

See the LICENSE.txt file for license information.

Contributor(s):
Damiano Lombardi, Ruiyang DAI

"""

import numpy as np

"""
Exercice 6 [Alg\`ebre lin\'eaire].

On pose,

A = ( [1, -1,  7], [-4, 2, 11], [8, 0, 3] )
B = ( [3, -2, -1], [ 7, 8,  6], [5, 1, 3] )

Trouver les lignes d'instructions permettant de:

1. Multiplier chaque \'el\'ement de A par le nombre \pi.
2. R\'ealiser la multiplication terme \`a terme de A par B.
3. D\'eterminer le nombre de lignes et de colonnes de A et le nombre d'\'el\'ements de B.
4. Calculer les matrices AB^T, Id-BB^T.
5. Multiplier A \`a droite par la matrice de m\^eme taille constante \`a 1.
6. Extraire les \'el\'ements diagonaux de A.
7. Annuler la diagonale de B.
8. Construire par concat\'enation la matrice (A B) puis la matrice (A^T B^T)^T.
9. Extraire de B = (b_{ij})_{1 <= i,j <= 3} les \'el\'ements dont les indices de lignes
   et de colonnes sont impairs.

Mots clefs: np.shape, np.size, .T, np.concatenate (Python)
"""
print("\nExercice 6:")
print("Linear algebra: \n")

# Declaration
A = np.array([[1, -1,  7], [-4, 2, 11], [8, 0, 3]])
B = np.array([[3, -2, -1], [ 7, 8,  6], [5, 1, 3]])

# A = \pi * A
A = A * np.pi

# Element-wise multiplication of A and B
# Comments:
# The expression A * B represents the element-wise multiplication 
# of matrix A by the transpose of matrix B. 
# In other words, it multiplies each corresponding element of A 
# with the corresponding element of B.
# Note: This multiplication is also called Hadamard product.
element_wise_multiply = A * B

# Get the number of rows and clumns in A
nl, nc = A.shape

# Get the total number of elements in B
nn = B.size

# Matrix multiplication of A and B transpose
matrix_multiply = np.dot(A, B.T)
# Alternatively, you can use the @ operator for matrix multiplication
# result = A @ B.T

# Create an identity matrix with the same dimensions as B
identity_B = np.eye(B.shape[0]) - np.dot(B, B.T)

# Matrix multiplication of A and a matrix of ones with the same dimensions as A
A_ones = np.dot(A, np.ones(A.shape))

# Get the diagonal elements of A
A_diag = np.diag(A)

# Subtract the diagonal elements of B from B
B = B - np.diag(np.diag(B))

# Concatenate matrices A and B horizontally
AB_horizontal = np.hstack((A, B))

# Concatenate matrices A and B vertically
AB_vertical = np.vstack((A, B))

# Extract a submatrix from B (1st and 2nd rows, 1st and 2nd columns)
# The syntax for slicing in NumPy is start:stop:step, 
# and it allows you to extract a portion (submatrix) of the original array.
# 0:3:2 for rows means starting from row 0 (inclusive), stopping at row 3 (exclusive), 
# and using a step of 2. So, it selects rows 0 and 2 from the original matrix B.
# 0:3:2 for columns means starting from column 0 (inclusive), 
# stopping at column 3 (exclusive), and using a step of 2. 
# So, it selects columns 0 and 2 from the rows selected in the previous step.
B_submatrix = B[0:3:2, 0:3:2]

print("1. A = \pi * A:")
print(A)

print("\n2. New matrix, element-wise multiplication of A and B:")
print(element_wise_multiply)

print("\n3. Number of rows in A:", nl)
print("   Number of columns in A:", nc)
print("   Total number of elements in B:", nn)

print("\n4. New matrix, matrix multiplication of A and B transpose:")
print(matrix_multiply)

print("\n   New matrix, Identity(B) - B * B transpose:")
print(identity_B)

print("\n5. New matrix, Mat mult. of A and a mat of ones with the same dimensions as A:")
print(A_ones)

print("\n6. Diagonal elements of A:")
print(A_diag)

print("\n7. The matrix B, cancellation of diagonal elements of B:")
print(B)

print("\n8. Horizontal concatenation of A and B:")
print(AB_horizontal)

print("\n   Vertical concatenation of A and B:")
print(AB_vertical)

print("\n9. Submatrix of B (1st and 3rd rows, 1st and 3rd columns):")
print(B_submatrix)
