import numpy as np
import matplotlib.pyplot as plt
from generation import generer_approbation_profil, generer_ordre_profil
from parpair import calcul_approbation, calcul_ordre
from phi2 import phi2_approbation, phi2_ordre

# Générer des profils d'approbation et d'ordre pour différentes valeurs de polarisation :
def simuler_phi2(n, m, repetitions = 1000):
    p_valeurs = np.linspace(0, 1, 21)
    phi_moyen = []

    for p in p_valeurs:
        valeurs = []
        for _ in range(repetitions):
            profil = generer_approbation_profil(n, m, polarisation = p)
            phi = phi2_approbation(profil)
            valeurs.append(phi)
        phi_moyen.append(np.mean(valeurs))
    return p_valeurs, phi_moyen

n = 50
m = 5

p_valeurs, phi_moyen = simuler_phi2(n, m)
plt.plot(p_valeurs, phi_moyen)
plt.xlabel('Paramètres de polarisation p')
plt.ylabel('φ₂(p)')
plt.title('volution de la polarisation')

plt.show()