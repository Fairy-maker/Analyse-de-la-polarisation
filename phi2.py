import numpy as np
from generation import generer_profil, TypeDeVote
from parpair import ensemble_des_diff_absolue

def phi2(profil, type_de_vote):
    """Calcule la valeur de Phi2 pour un profil donné et un type de vote spécifié."""
    n, m = profil.shape
    d_valeurs = ensemble_des_diff_absolue(profil, type_de_vote)
    return 1 - np.sum(d_valeurs) / (n * (m*(m-1)))


# Exemple :

if __name__ == "__main__":
    for type_de_vote in TypeDeVote:
        print(f"Type de vote: {type_de_vote.name}")
        profil = generer_profil(type_de_vote=type_de_vote, n=10, m=5, polarisation=0.0)
        print("Phi2 approbation pour profil non polarise:", phi2(profil, TypeDeVote.APPROBATION))

if __name__ == "__main__":
    for type_de_vote in TypeDeVote:
        print(f"Type de vote: {type_de_vote.name}")
        profil = generer_profil(type_de_vote=type_de_vote, n=10, m=5, polarisation=1.0)
        print("Phi2 approbation pour profil polarise:", phi2(profil, TypeDeVote.APPROBATION))