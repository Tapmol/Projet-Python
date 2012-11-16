from Tkinter import *
from tkFileDialog import *
from pgm import *
from traitement import *
from luminosite import *
from negatif import *
from flou import *
from filtrage_median import *
from bruit import *
from contraste import *

def ouvrir_image (zone_image):
    nom_fichier=askopenfilename()
    if nom_fichier[-3:]!='pgm': #si l'extension du fichier ne correspond pas a pgm on sort (en supposant qu'on accepte que les fichiers pgm)
        return
    if len(nom_fichier)!=0:
        zone_image['nom_fichier']=nom_fichier
        afficherImage(zone_image)
    
def afficherImage(zone_image):
        photo=PhotoImage(file=zone_image['nom_fichier'])
        zone_image['image']=photo
        zone_image['canvas'].configure(width=zone_image['image'].width(),height=zone_image['image'].height())
        zone_image['canvas'].create_image(0,0,anchor=NW, image=zone_image['image'])
        zone_image['canvas'].pack()
    
def appliquer_symetrie(zone_image):
    if zone_image['nom_fichier']== '':  #On verifie qu'un fichier est bien ouvert
        return
    tableau=lire_fichier_pgm_binaire(zone_image['nom_fichier'])
    symetrie(tableau)
    creer_image_pgm_binaire(tableau, "tmp.pgm")
    zone_image['tableau']=tableau
    zone_image['nom_fichier']="tmp.pgm"
    afficherImage(zone_image)

def augmenter_luminosite (zone_image):
    if zone_image['nom_fichier']== '':
        return
    tableau=lire_fichier_pgm_binaire(zone_image['nom_fichier'])
    luminosite(tableau,10)
    creer_image_pgm_binaire(tableau, "tmp.pgm")
    zone_image['tableau']=tableau
    zone_image['nom_fichier']="tmp.pgm"
    afficherImage(zone_image)

def reduire_luminosite (zone_image):
    if zone_image['nom_fichier']== '':
        return
    tableau=lire_fichier_pgm_binaire(zone_image['nom_fichier'])
    luminosite(tableau,-10)
    creer_image_pgm_binaire(tableau, "tmp.pgm")
    zone_image['tableau']=tableau
    zone_image['nom_fichier']="tmp.pgm"
    afficherImage(zone_image)

def inversion (zone_image):
    if zone_image['nom_fichier']== '':
        return
    tableau=lire_fichier_pgm_binaire(zone_image['nom_fichier'])
    negatif(tableau)
    creer_image_pgm_binaire(tableau, "tmp.pgm")
    zone_image['tableau']=tableau
    zone_image['nom_fichier']="tmp.pgm"
    afficherImage(zone_image)

def flou (zone_image):
    if zone_image['nom_fichier']== '':
        return
    tableau=lire_fichier_pgm_binaire(zone_image['nom_fichier'])
    floutage(tableau)
    creer_image_pgm_binaire(tableau, "tmp.pgm")
    zone_image['tableau']=tableau
    zone_image['nom_fichier']="tmp.pgm"
    afficherImage(zone_image)
    
def filtrage_median (zone_image):
    if zone_image['nom_fichier']== '':
        return
    tableau=lire_fichier_pgm_binaire(zone_image['nom_fichier'])
    filtrage(tableau)
    creer_image_pgm_binaire(tableau, "tmp.pgm")
    zone_image['tableau']=tableau
    zone_image['nom_fichier']="tmp.pgm"
    afficherImage(zone_image)
    

def sauver_sous(zone_image):
    if zone_image['nom_fichier']=='':  #Si aucun fichier n'est ouvert on sort
        return 
    tableau_modifie=zone_image['tableau']
    nom=asksaveasfilename()
    if len(nom)==0:  #Si on clique sur le bouton Annuler on sort
        return
    creer_image_pgm_binaire(tableau_modifie,nom)

def bruit_poivre_et_sel (zone_image):
    if zone_image['nom_fichier']== '':
        return
    tableau=lire_fichier_pgm_binaire(zone_image['nom_fichier'])
    bruit(tableau)
    creer_image_pgm_binaire(tableau, "tmp.pgm")
    zone_image['tableau']=tableau
    zone_image['nom_fichier']="tmp.pgm"
    afficherImage(zone_image)

def augmenter_contraste (zone_image):
    if zone_image['nom_fichier']== '':
        return
    tableau=lire_fichier_pgm_binaire(zone_image['nom_fichier'])
    contraste(tableau)
    creer_image_pgm_binaire(tableau, "tmp.pgm")
    zone_image['tableau']=tableau
    zone_image['nom_fichier']="tmp.pgm"
    afficherImage(zone_image)


