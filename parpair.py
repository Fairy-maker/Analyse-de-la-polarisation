import numpy as np
from generation import generer_approbation_profil, generer_ordre_profil


#Calcul de la distance d'approbation :
def calcul_approbation(profil):
    n, m =profil.shape
    d_valeurs = []

    for k in range(m):
        for l in range(k+1, m):
            n_kl = np.sum((profil[:,k] == 1) & (profil[:,l] == 0))
            n_lk = np.sum((profil[:,l] == 1) & (profil[:,k] == 0))

            d = abs(n_kl - n_lk)

            d_valeurs.append(d)
    return np.array(d_valeurs)

#Exemple : 
if __name__ == "__main__":
    p = generer_approbation_profil(10, 5, polarisation = 0.5)
    print(calcul_approbation(p))

#Calcul de la distance d'ordre :
def calcul_ordre(profil):
    n, m = profil.shape
    d_valeurs = []

    for k in range(m):
        for l in range(k+1, m):

            n_kl = 0
            n_lk = 0

            for vote in profil:
                position_k = np.where(vote == k)[0][0]
                position_l = np.where(vote == l)[0][0]

                if position_k < position_l:
                    n_kl += 1
                else:
                    n_lk += 1
            d = abs(n_kl - n_lk)
            d_valeurs.append(d)
    return np.array(d_valeurs)
        
#Exemple : 
if __name__ == "__main__":
    p = generer_ordre_profil(10, 5, polarisation = 0.5)
    print(calcul_ordre(p))
            
