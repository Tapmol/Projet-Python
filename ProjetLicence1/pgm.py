# -*- coding:utf-8 -*-

from tableaux2D import *
from string import *

# lecture/ecriture de fichier pgm binaire

def creer_fichier(l,h,nom,type):
    file = open(nom,'w')
    file.write(type + '\n')
    file.write(str(l) + ' ' + str(h) + '\n')
    file.write('255 \n')
    return file

def creer_image_pgm_binaire(t, nom):
    h = len(t)
    l = len(t[0])
    file =creer_fichier(l,h,nom,'P5')
    for i in range(h):
        for j in range(l):
            file.write('%c'%t[i][j]) #transforme un entier entre 0 et 255 en octet
    file.close()


def lire_fichier_pgm_binaire (nom):
    f = open (nom)

  #lecture du "magic number" P5
    mode = f.readline()
  
  #lecture des dimensions (il faut sauter les éventuelles lignes de commentaire)
    dim = f.readline()
    while dim[0] == '#':
        dim = f.readline()
    t_dim = split(dim)
    largeur = int(t_dim[0])
    hauteur = int(t_dim[1])

  # création du tableau image
    t_image = creer_tableau(hauteur, largeur, 0)

  # lecture de la valeur maximale d'un niveau de gris (255)
    val_max = f.readline()

    for i in range(hauteur):
        for j in range(largeur):
            t_image[i][j] = ord(f.read(1)) # transforme un octet en entier

    f.close()
    return t_image











