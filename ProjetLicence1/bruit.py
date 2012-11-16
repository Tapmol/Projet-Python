from randomlibs import *

#randomlibs a ete utilise pour les fonctions randint et choice

def bruit(t):
    couleur=[0,255]
    nb_cases=len(t)*len(t[0])
    pixels_modifies=nb_cases*1//100 #on determine 1% du nombre de cases de t
    while pixels_modifies>0:
        m=randint(0,len(t)-1) #on choisit aleatoirement une coordonnee hauteur
        n=randint(0,len(t[0])-1) #on choisit aleatoirement une coordonee largeur
        s=choice(couleur) #on prend aleatoirement la valeur 0 ou 255
        t[m][n]=s
        pixels_modifies-=1

    
    


    
