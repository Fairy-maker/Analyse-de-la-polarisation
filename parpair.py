import numpy as np
from generation import generer_profil, TypeDeVote

def nbr_votantes_pref(profil, k, l, type_de_vote):
    """Étant donné un profil et deux candidates d'indice k et l, cette méthode 
    retourne de nombre de votantes qui préfèrent ck à cl, étant donné le type de vote.
    """
    match type_de_vote:
        case TypeDeVote.APPROBATION:
            return np.sum((profil[:,k] == 1) & (profil[:,l] == 0))
        case TypeDeVote.ORDRE_TOTAUX:
            n_kl = 0
            for vote in profil:
                position_k = np.where(vote == k)[0][0]
                position_l = np.where(vote == l)[0][0]
                if position_k < position_l:
                    n_kl += 1
            return n_kl


def diff_absolue(profil, k, l, type_de_vote):
    n_kl = nbr_votantes_pref(profil, k, l, type_de_vote)
    n_lk = nbr_votantes_pref(profil, l, k, type_de_vote)
    return abs(n_kl - n_lk)


def ensemble_des_diff_absolue(profil, type_de_vote):
    n, m = profil.shape
    d_valeurs = np.zeros((m,m))
    for k in range(m):
        for l in range(k+1, m):
            d = diff_absolue(profil, k, l, type_de_vote)
            d_valeurs[k][l] = d
            d_valeurs[l][k] = d
    return d_valeurs


def ensemble_des_diff_absolue_approbation(profil):
    return ensemble_des_diff_absolue(profil, TypeDeVote.APPROBATION)


def ensemble_des_diff_absolue_ordre_totaux(profil):
        return ensemble_des_diff_absolue(profil, TypeDeVote.ORDRE_TOTAUX)


#Exemple : 
if __name__ == "__main__":
    print("Profils polarisés :")
    for type_de_vote in TypeDeVote:
        print(f"Type de vote: {type_de_vote.name}")
        p = generer_profil(n=10, m=5, polarisation=1.0, type_de_vote=type_de_vote)
        print(ensemble_des_diff_absolue(p, type_de_vote))

        
#Exemple : 
if __name__ == "__main__":
    print("Profils non polarisés :")
    for type_de_vote in TypeDeVote:
        print(f"Type de vote: {type_de_vote.name}")
        p = generer_profil(n=10, m=5, polarisation=0.0, type_de_vote=type_de_vote)
        print(ensemble_des_diff_absolue(p, type_de_vote))
