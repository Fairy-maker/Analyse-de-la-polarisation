import numpy as np

# Q1 : Générer aléatoirement un profil dans A^n : 
def generer_approbation_profil(n, m, polarisation = 0.0, bruit = 0.05): # n = nombre de votantes, m = nombre de candidates
    a = np.random.randint(0, 2, m)
    a_barre = 1 - a
    profil = []

    for _ in range(n):
        if np.random.rand() < polarisation:
            vote = a_barre.copy()
        else:
            vote = a.copy()
        
        # ajout du bruit
        for j in range(m):
            if np.random.rand() < bruit:
                vote[j] = 1 - vote[j]
        
        profil.append(vote)
    return np.array(profil)

# Exemple :
#Pas très polarisé :
if __name__ == "__main__":
    p = generer_approbation_profil(10, 5, polarisation = 0.1)
    print(p)

#Très polarisé :
if __name__ == "__main__":
    p = generer_approbation_profil(10, 5, polarisation = 0.5)
    print(p)

# Q2 : Générer aléatoirement un profil dans L^n : 
def generer_ordre_profil(n, m, polarisation = 0.0, bruit = 0.05):
    ordre = np.random.permutation(m)
    ordre_barre = ordre[::-1]
    profil = []

    for _ in range(n):
        if np.random.rand() < polarisation:
            vote = ordre_barre.copy()
        else:
            vote = ordre.copy()
        
        if np.random.rand() < bruit:
            i, j = np.random.choice(m, 2, replace=False)
            vote[i], vote[j] = vote[j], vote[i]
        profil.append(vote)

    return np.array(profil)

# Exemple :
#Pas très polarisé :
if __name__ == "__main__":
    p = generer_ordre_profil(10, 5, polarisation = 0.1)
    print(p)

#Très polarisé :
if __name__ == "__main__":
    p = generer_ordre_profil(10, 5, polarisation = 0.5)
    print(p)   
