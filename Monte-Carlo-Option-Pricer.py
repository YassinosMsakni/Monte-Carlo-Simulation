#################################################################################
# Simulation Monte Carlo pour calculer le Prix d'une option Call / Put européenne
#################################################################################

from math import sqrt #Importation de la fonction sqrt du module math
from math import exp #Importation de la fonction exp du module math

from random import random

from scipy.stats import norm

# Génération d'une variable aléatoire suivant Loi Normale Gaussienne centrée réduite
# norm.ppf() fonction Inverse de la fonction de répartition Gaussienne

def VarGaussienne():
    
    a = random()
    
    return norm.ppf(a, 0, 1)

# Fonction du Prix Forward de l'actif suivant le Modèle GBM
# Calculer S(T)
# vg = variable aléatoire gaussienne

def FwdGBM(S, mu, sigma, T, vg): # vg: variable gaussienne normale centrée réduite
    Fwd = S*exp((mu - sigma**2 / 2)*T + sigma*sqrt(T)*vg)
    return Fwd

# Calculer La Prime de Call
#--------------------------

# Fonction MaxSK_Call = Max((S-K), 0) pour calculer Prime Call

def MaxSK_Call(S,K): # S: Spot (à l'échéance), K: Strike
    if (S>=K):
      VMax = S-K
    else:
        VMax = 0 
    return(VMax)

# Calculer la valeur moyenne qui donne le prix de l'Option suivant Monte Carlo

# Option Call EURUSD

S = 1.135 # Spot EURUSD

K = 1.1432
sigma = 6.16/100
T = 0.25 # 3 mois
r = 2.60/100 # Taux sans risque $
q = -0.31/100 # Taux sans risque €

mu = r - q

N = 100000
PrimeSomme = 0

for i in range(0, N):
    
    vg = VarGaussienne()

    fwd = FwdGBM(S, mu, sigma, T, vg)
    
    PrimeSomme = PrimeSomme +  MaxSK_Call(fwd,K)

PrimeCall_estimee = exp(-r*T)*(PrimeSomme / N)

print("Prime Call estimée: ", PrimeCall_estimee)

# Calcul de l'erreur relative
#----------------------------

from ModuleBlackScholes import bs_call #Importation bs_call

Prime_call = bs_call(S,K,sigma,T,r,q)

print("Prime Call: ", Prime_call)

# Analyse erreur

Erreur_relatif = (PrimeCall_estimee - Prime_call) / Prime_call

print("Erreur relative: ", "%.3f" % (Erreur_relatif*100), "%")
print("1/sqrt(N): ", "%.3f" % (100/sqrt(N)), "%")
