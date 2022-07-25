import numpy as np
from numpy import sin
from numpy import cos

from math import sqrt

# Fonction sinus
#---------------

def func(x):
    return sin(x) + 0.5*x

a = 0.5 # integral limits start
b = 9.5 # integral limits stop

#Xmin = 0
#Xmax = 10

# Intégrale avec méthode Monte Carlo
#-----------------------------------

# Trouver Ymax

Ix = np.linspace(a, b, 200)

#print(Ix)

Iy = func(Ix)

#print(Iy)

Ymax = max(Iy)
print("Ymax", Ymax)

from random import random

N = 1000000

compteur = 0
for i in range(0, N):
    
    xi = a + random()*(b-a)
    yi = random()*Ymax
    
    f_of_x = func(xi)
    
    if (yi < f_of_x):
        compteur = compteur + 1

Aire_rectangle = Ymax*(b-a)

Integrale_estime = (compteur / N) * Aire_rectangle

print("Intégrale estimée: ", Integrale_estime)

# Calcul de l'erreur relative
#----------------------------
# F(x) fonction primitive de sin(x) + 0,5x
# F(x) = -cos(x) + 0.25x**2

def Primitivefunc(x):
    return -cos(x) + 0.25*(x**2)

# Intégrale fournie par F(x) :

v_integrale = Primitivefunc(b) - Primitivefunc(a)

print("Intégrale valeur exacte", v_integrale)

# Analyse erreur

Erreur_relatif = abs(Integrale_estime - v_integrale) / v_integrale

print("Erreur relative: ", "%.3f" % (Erreur_relatif*100), "%")
print("1/sqrt(N): ", "%.3f" % (100/sqrt(N)), "%")
