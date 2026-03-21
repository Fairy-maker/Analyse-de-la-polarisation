import numpy as np
from generation import generer_approbation_profil, generer_ordre_profil
from parpair import calcul_approbation, calcul_ordre

# Calcul de Phi2 pour les profils d'approbation :
def phi2_approbation(profil):
    n, m = profil.shape
    d_valeurs = calcul_approbation(profil)
    return np.sum(n - d_valeurs) / (n * (m*(m-1)/2))

# Calcul de Phi2 pour les profils d'ordre :
def phi2_ordre(profil):
    n = len(profil)
    m = len(profil[0])
    d_valeurs = calcul_ordre(profil)
    return np.sum(n - d_valeurs) / (n * (m*(m-1)/2))

# Exemple :
profil = generer_approbation_profil(10, 5, polarisation = 0.5)
print("Phi2 approbation:", phi2_approbation(profil))

profil = generer_ordre_profil(10, 5, polarisation = 0.5)
print("Phi2 ordre:", phi2_ordre(profil))
