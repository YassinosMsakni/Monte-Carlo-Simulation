# Simulation Monte Carlo
# Estimateur de pi
########################

from math import pi
from math import sqrt

from random import random

N = 1000000

compteur = 0
for i in range(0, N):
    
    x = random()
    y = random()
    
    if ((x**2 + y**2) <= 1):
        compteur = compteur + 1

pi_estime = (compteur / N) * 4

print("valeur de pi estimée: ", pi_estime)

# Calcul de l'erreur relative
#----------------------------

print("valeur de pi: ", pi)

Erreur_relative = (pi_estime - pi) / pi

print("Erreur relative:", "%.3f" % (100*Erreur_relative), "%")

print ("1/sqrt(N) :", "%.3f" % (100/sqrt(N)), "%" )