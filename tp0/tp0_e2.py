"""
MU4MA006 - Travaux pratiques 0
2023-2024  Sorbonne Universite

See the LICENSE.txt file for license information.

Contributor(s):
Damiano Lombardi, Ruiyang DAI

"""

import numpy as np

"""
Exercice 2 [\'Ecrire et tester une fonction].

Ecrire une fonction qui calcule les moyennes arithm\'etique et g\'eom\'etrique de
deux r\'eels. Puis la tester avec les couples de valeurs suivants (3,2) et (5,-6).

M\'emo: on appelle moyenne arithm\'etique de a et b la quantit\'e (a+b)/2 et,
quand elle existe, moyenne g\'eom\'etrique la quantit\'e \sqrt(ab).


Mots clefs: def, np.sqrt if (Python)
"""
print("Exercie 2:")
def calcuer_moyennes(a, b):
    # Calcule le moyen arithm\'etique et le moyen g\'eom\'etrique de deux nombre.

    # param a: premier  nombre
    # param b: deuxième nombre
    print(f"Le couple des valeurs est: ({a}, {b})")

    moyen_arithmetique = (a + b) / 2.0
    if a + b >= 0.0:
        moyen_geometrique = np.sqrt(a * b) / 2.0
        print(f"Le moyen arithmétique est: {moyen_arithmetique}")
        print(f"Le moyen géométrique  est: {moyen_geometrique}")
    else:
        print(f"Le moyen arithmétique est: {moyen_arithmetique}")
        print("Le moyen géométrique exist pas.")

# Nous appelons la fonction
calcuer_moyennes(3,  2)
calcuer_moyennes(5, -6)
