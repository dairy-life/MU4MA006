"""
MU4MA006 - Travaux pratiques 0
2023-2024  Sorbonne Universite

See the LICENSE.txt file for license information.

Contributor(s):
Damiano Lombardi, Ruiyang DAI

"""

import numpy as np

"""
Exercice 5 [Normes vectorielles].

On note u, v et w les vecteurs suivants,

u = ( 1, -1, 2)^T,
v = (10, -1, 3)^T,
u = ( 5, -1, 4)^T.

Calculer 3u, norm2(u), 2u-v+5w, norm1(2u-v+5w), normInfini(w-4v) et 
<u,v> le produit scalaire.

Mots clefs: np.linalg.norm, np.dot (Python)
"""
print("Exercie 5:")
print("Calcul des vecteurs et de leurs normes:")
u = np.array([ 1, -1, 2])
v = np.array([10, -1, 3])
w = np.array([ 5, -1, 4])

print("vector u:", u)
print("vector v:", v)
print("vector w:", w)
print("")

vec1 = 3*u
vec2 = 2*u-v+5*w
vec3 = w-4*v

print("vector 3*u:",       vec1)
print("vector 2*u-v+5*w:", vec2)
print("vector w-4*v:",     vec3)
print("")

norm2_vec1 = np.linalg.norm(u, 2)
norm1_vec2 = np.linalg.norm(vec2, 1)
normI_vec3 = np.linalg.norm(vec3, np.inf)

produit_scalaire = np.dot(u,v)

print("The results:")
print("3u: ", vec1)
print("||u||_2: ", norm2_vec1)
print("2u-v+5w: ", vec2)
print("||2u-v+5w||_1: ", norm1_vec2)
print("||w-4v||_inf: ", normI_vec3)
print("le produit scalaire <u,v>: ", produit_scalaire)
