# Analyse-de-la-polarisation
<p style="text-align:justify;"> Ce projet avait pour objectif d’étudier la polarisation des préférences exprimées lors de processus électoraux. Nous avions un ensemble de votantes et de candidates et différents processus de votes. Une élection était polarisée lorsque l’électorat pouvait être divisé en deux clusters de votantes distincts. Pour cela différentes techniques de distance et de clusterisation ont été utilisées dans notre projet tels que les distances de Hamming, de Spearman ou encore la clusterisation K-Means.</p>

## Structure du projet 
```
projet
├── question 1/ 
├── question 2/
├── question 3/
├── question 8/
├── question 12/
├── question 13/
├── question 14/
└── question 15/
```
Il est important de noter que les questions non présente dans le fichier projet.ipynb sont des questions de rédaction mise dans notre rapport. 

## Prérequis 
- Java Python 3 ou version compatible avec le projet
- VS Code (si possible)
- Jupyter Notebook

## Installation Jupyter depuis le terminal : 
- Pour pouvoir exécuter notre projet, vous devez tout d'abord installer jupyter sur votre ordinateur depuis votre terminal. Pour cela, vous devez exécuter les commandes suivantes :
   `pip3 install notebook`

  `pip3 install jupyterlab`
## Installation 
### Cloner le repo
 `git clone <repo-url>`
 
 `cd Analyse-de-la-polarisation`

 ## Lancement du projet 
  ### Convertir le notebook Jupyter (.ipynb) en fichier python(.py) : 
  - Depuis le terminal, vous devez convertir le notebook Jupyter en fichier python exécutable grâce à la commande :
    `python3 -m nbconvert --to script projet.ipynb`
  ### Exécuter le fichier python :
  - Pour exécuter le fichier ipynb maintenant transformé en fichier python, vous devez entrer la commande :
    `python3 projet.py`

**Auteur :** BAIGNERES Clara, BENAMEUR Féryel, BOUCHERON Lucie 
