# -*- coding:utf-8 -*-
from Tkinter import *
from tkFileDialog import *
from pgm import *
from interface import *

fen=Tk()

#la fonction pointeur a ete trouvee sur le net

def pointeur(event):
    chaine.configure(text="Souris positionnee en X = "+str(event.x)+", Y = "+str(event.y))

zone_image={'cadre':None, 'image':None, 'canvas':None, 'nom_fichier':"", 'tableau':""}

#Creation du menu

menu=Menu(fen)
fen.config(menu=menu)

fichiermenu=Menu(menu)
menu.add_cascade(label="Fichier", menu=fichiermenu)
fichiermenu.add_command(label="Ouvrir...", command=lambda:ouvrir_image(zone_image))
fichiermenu.add_separator()
fichiermenu.add_command(label="Sauver sous...", command=lambda:sauver_sous(zone_image))
fichiermenu.add_separator()
fichiermenu.add_command(label="Quitter",command=fen.destroy)


traitementmenu=Menu(menu)
menu.add_cascade(label="Traitement d'image", menu=traitementmenu)
traitementmenu.add_command(label="Symetrie", command=lambda:appliquer_symetrie(zone_image))
traitementmenu.add_separator()
traitementmenu.add_command(label="Augmenter Luminosite", command=lambda:augmenter_luminosite(zone_image))
traitementmenu.add_separator()
traitementmenu.add_command(label="Reduire Luminosite", command=lambda:reduire_luminosite(zone_image))
traitementmenu.add_separator()
traitementmenu.add_command(label="Negatif", command=lambda:inversion(zone_image))
traitementmenu.add_separator()
traitementmenu.add_command(label="Flou", command=lambda:flou(zone_image))
traitementmenu.add_separator()
traitementmenu.add_command(label="Filtrage Median", command=lambda:filtrage_median(zone_image))
traitementmenu.add_separator()
traitementmenu.add_command(label="Bruit Poivre et Sel", command=lambda:bruit_poivre_et_sel(zone_image))
traitementmenu.add_separator()
traitementmenu.add_command(label="Augmenter Contraste", command=lambda:augmenter_contraste(zone_image))

#creation du canevas

c=Canvas(fen)      
c.bind("<Button-1>",pointeur)
c.pack()
zone_image['canvas']=c

#creation de la zone de texte

chaine=Label(fen)
chaine.pack()

fen.mainloop()
