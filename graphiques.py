import numpy as np
import matplotlib.pyplot as plt
from generation import generer_profil, TypeDeVote
from parpair import ensemble_des_diff_absolue
from phi2 import phi2

# Générer des profils d'approbation et d'ordre pour différentes valeurs de polarisation :
def simuler_phi2(type_de_vote, n, m, repetitions = 1000):
    p_valeurs = np.linspace(0, 1, 21)
    phi_moyen = []

    for p in p_valeurs:
        valeurs = []
        for _ in range(repetitions):
            profil = generer_profil(type_de_vote=type_de_vote, n=n, m=m, polarisation=p)
            phi = phi2(profil, type_de_vote)
            valeurs.append(phi)
        phi_moyen.append(np.mean(valeurs))
    return p_valeurs, phi_moyen


n = 50
m = 5

for type_de_vote in TypeDeVote:
    p_valeurs, phi_moyen = simuler_phi2(type_de_vote=type_de_vote, n=n, m=m)
    plt.plot(p_valeurs, phi_moyen)
    plt.xlabel('Paramètres de polarisation')
    plt.ylabel('φ₂(p)')
    plt.title(f'Évolution de la polarisation - {type_de_vote.name}')
    plt.show()

