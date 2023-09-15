"""
MU4MA006 - Travaux pratiques 0
2023-2024  Sorbonne Universite

See the LICENSE.txt file for license information.

Contributor(s):
Damiano Lombardi, Ruiyang DAI

"""

import numpy as np

"""
Exercice 13

On s'int\'eresse de nouveau \`a l'estimation du nombre d'or, 
$\phi = ( 1+\sqrt(5) )/2$. 
On d\'efinit la suite $(F_n)_{n>=1}$ par $F_1=F_2=1$ 
et $F_n = F_{n-1} + F_{n-2}$ pour $n>2$.

1. Ecrire une fonction qui prend en entr\'ee un entier $N>=1$ et qui renvoie $F_N$.
2. V\'erifier num\'eriquement le r\'esultat suivant: 
\phi = \lim_{n\to\infinity} F_{n+1}/F_{n}.

"""
print("\nExercice 13:")
print("\nFibonacci number: \n")

def Fibonacci(n):
    # Function Fibonacci

    # param n: the index of the Fibonacci number 
    # return Fn: n-th Fibonacci number
    Fn = 1
    Fm = 1  # Fn-1

    for i in range(3, n + 1):
        aux = Fn
        Fn = Fn + Fm
        Fm = aux

    return Fn

# Le nombre d'or
nbOr = (1 + 5 ** 0.5) * 0.5

# The number of Fibonacci numbers
n_values = [10, 25, 50, 100]

for n in n_values:
    F_n = Fibonacci(n + 1)
    l = F_n / Fibonacci(n)
    absolute_difference = abs(l - nbOr)
    print(f"For n = {n}:")
    print(f"Computed l: {l}")
    print(f"Absolute Difference: {absolute_difference}\n")
