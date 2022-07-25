import numpy as np

from numpy import exp

from math import pi
from math import sqrt

# Fonction exponentiel
#---------------------

def func(x):
    return 0.5 * exp(x) + 1

a = 0.5 # integral limits start
b = 1.5 # integral limits stop

# Intégrale avec méthode Monte Carlo
#-----------------------------------

# Trouver Ymax

Ix = np.linspace(a, b, 2000)
Iy = func(Ix)

Ymax = max(Iy)
print("Ymax", Ymax)

from random import random

N = 100000

compteur = 0
for i in range(0, N):
    
    xi = a + random()*(b-a)
    yi = random()*Ymax
    
    f_of_x = func(xi)
    
    if (yi < f_of_x):
        compteur = compteur + 1

Aire = Ymax*(b-a)

Integrale_estimee = (compteur / N) * Aire

print("Intégrale estimée: ", Integrale_estimee)

# Calcul de l'erreur relative
#----------------------------
# F(x) fonction primitive de 0,5exp(x) + 1
# F(x) = 0,5exp(x) + x

def Primitivefunc(x):
    return 0.5*exp(x) + x

# Intégrale fournie par F(x) :

v_integrale = Primitivefunc(b) - Primitivefunc(a)

print("Intégrale valeur exacte", v_integrale)

Erreur_relatif = (Integrale_estimee - v_integrale) / v_integrale

print("Erreur relative: ", "%.3f" % (Erreur_relatif*100), "%")
print("1/sqrt(N): ", "%.3f" % (100/sqrt(N)), "%")
