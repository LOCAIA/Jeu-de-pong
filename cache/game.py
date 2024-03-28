#!/usr/bin/env python3
# coding: utf8
from tkinter import *
from random import randrange
import tkinter.messagebox as mbox
import configparser

# Lecture des paramètres depuis le fichier texte
config = configparser.ConfigParser()
config.read("parametre.txt")

# Des constantes (les valeurs ne changeront pas durant le jeu).
HAUTEUR = 600       # Hauteur de l'aire de jeu.
LARGEUR = 600       # Largeur de l'aire de jeu.
TAILLE_BALLE = 10   # Diamètre de la balle.
DXY = TAILLE_BALLE  # Déplacement maximum de la balle, quel que soit l'axe.
LARGEUR_RAQUETTE = TAILLE_BALLE         # Dimensions de
HAUTEUR_RAQUETTE = 6 * TAILLE_BALLE     # la "raquette".
xG_RAQUETTE = 50    # Coordonnée X du bord gauche de la raquette.
xD_RAQUETTE = xG_RAQUETTE + LARGEUR_RAQUETTE    # Idem pour le bord droit.

# Le dictionnaire qui gère la configuration "dynamique" du jeu. Les clefs
# correspondent à des valeurs qui pourront évoluer durant une partie.
config_params = { "vitesse": config.getint("Parametres", "VolumeSonPourcent"),           # "Vitesse initiale" de la balle.
           "vitesse_min" : config.getint("Parametres", "VolumeSonMinPourcent"),       # "Vitesse minimale" de la balle.
           "vitesse_max" : config.getint("Parametres", "VolumeSonMaxPourcent"),     # "Vitesse maximale" de la balle.
           "balles_touchées" : 0,   # Pour compter les réussites.
           "balles_manquées" : 0,   # Pour compter les échecs.
           "jeu_en_pause" : False,  # Le jeu est-il en pause ?
           "direction_raquette" : 0,# Mouvement raquette 0:immobile, -1:↑, 1:↓.
           "dx_balle" : 0,          # Déplacement en x de la balle.
           "dy_balle" : 0,          # Déplacement en y de la balle.
           "balle" : 0,             # L'identifiant Canvas de la balle.
           "raquette" : 0,          # L'identifiant Canvas de la raquette.
           "animation" : None       # Le "job" d'animation en cours.
}

# Fonctions
def construit_balle(x, y, couleur='yellow'):
    """Crée une balle dans un canevas"""
    return can.create_oval(x, y, x+TAILLE_BALLE, y+TAILLE_BALLE, fill=couleur, width=2)

def construit_raquette(x, y, couleur='black'):
    """Crée une raquette dans un canevas"""
    return can.create_rectangle(x, y, x+LARGEUR_RAQUETTE, y+HAUTEUR_RAQUETTE, fill=couleur, width=2)

def enfoncer(event):
    """Ce qu'il se passe lorsqu'on enfonce une touche"""
    touche = event.keysym
    if touche == "Up":
        config_params["direction_raquette"] = -1
    if touche == "Down":
        config_params["direction_raquette"] = 1
    if touche == "Right":
        config_params["vitesse"] = min(config_params["vitesse"] + 1, config_params["vitesse_max"])
    if touche == "Left":
        config_params["vitesse"] = max(config_params["vitesse"] - 1, config_params["vitesse_min"])

def relacher(event):
    """Ce qu'il se passe lorsqu'on relâche une touche"""
    config_params["direction_raquette"] = 0

def jouer(event=None):
    """Prépare et démarre une nouvelle partie"""
    # Le jeu démarre
    config_params["jeu_en_pause"] = False
    # On efface les éléments graphiques issus d'une éventuelle partie précédente.
    can.delete("all")
    # On interrompt tout éventuel cycle d'animation.
    if config_params["animation"] is not None:
        fen.after_cancel(config_params["animation"])
    # On crée de (nouvelles) balle et raquette.
    config_params["balle"] = construit_balle(LARGEUR-TAILLE_BALLE-1, randrange(0, LARGEUR-TAILLE_BALLE))
    config_params["raquette"] = construit_raquette(xG_RAQUETTE, (HAUTEUR-HAUTEUR_RAQUETTE)/2)
    # On détermine aléatoirement un vecteur de déplacement pour la balle.
    config_params["dx_balle"] = -DXY/4
    config_params["dy_balle"] = randrange(int(-DXY/2), int(DXY/2))
    # On anime le tout !
    animer()

def animer():
    """Gestion des déplacements des différents éléments graphiques"""
    # Coordonnées de la balle (coin en haut à gauche de la « bounding box »).
    balle = config_params["balle"]
    raquette = config_params["raquette"]
    dx = config_params["dx_balle"]
    dy = config_params["dy_balle"]
    xb, yb = can.coords(balle)[0], can.coords(balle)[1]
    # Coordonnée en Y de la raquette (idem).
    yr = can.coords(raquette)[1]
    # Gestion des rebonds de la balle.
    if xG_RAQUETTE <= xb <= xD_RAQUETTE and yr <= yb <= yr+HAUTEUR_RAQUETTE-TAILLE_BALLE:
        dx = -dx
        config_params["dx_balle"] = dx
        config_params["balles_touchées"] += 1
        touche_sv.set("Touché : {}".format(config_params["balles_touchées"]))
        dy = randrange(int(-DXY/2), int(DXY/2))  # Générer une nouvelle valeur de déplacement vertical aléatoire
        config_params["dy_balle"] = dy
    elif xb >= LARGEUR-TAILLE_BALLE or xb <= 0:
        dx = -dx
        config_params["dx_balle"] = dx
    elif yb <= 0 or yb >= HAUTEUR-TAILLE_BALLE:
        dy = -dy
        config_params["dy_balle"] = dy
    elif xb < xG_RAQUETTE:
        mbox.showinfo("Perdu !", "Oooops, vous ferez mieux la prochaine fois ! Pressez [Ctrl]+[J]")
        config_params["jeu_en_pause"] = True
        config_params["balles_manquées"] += 1
        manque_sv.set("Manqué : {}".format(config_params["balles_manquées"]))
    v = config_params["vitesse"]
    if v != 0:  # Vérifie si la vitesse n'est pas égale à zéro
        can.move(balle, dx*v/config_params["vitesse"], dy*v/config_params["vitesse"])     # Déplacement de la balle
    # Gestion des déplacements de la raquette
    if (yr > 0 and config_params["direction_raquette"] == -1) or (yr < HAUTEUR-HAUTEUR_RAQUETTE and config_params["direction_raquette"] == 1):
        # Déplacement de la raquette
        can.move(raquette, 0, config_params["direction_raquette"]*TAILLE_BALLE)
    if not config_params["jeu_en_pause"]:
        config_params["animation"] = can.after(20, animer)


def ecrire_scores():
    """Écrit les scores dans le fichier texte."""
    with open("log.txt", "w") as f:
        f.write("Dernier score : {}\n".format(config_params["balles_touchées"]))
        f.write("Dernières balles manquées : {}\n".format(config_params["balles_manquées"]))
        # Vous pouvez ajouter d'autres informations comme le meilleur score ici
        # Assurez-vous de les écrire dans le fichier texte

def quitter(event=None):
    """Fonction appelée lorsque le joueur quitte le jeu."""
    ecrire_scores()  # Écrire les scores dans le fichier texte
    fen.quit()

def regle_du_jeu():
    mbox.showinfo("Règle du jeu",
        """Ne ratez pas la balle !
Les fèches vers le haut et vers
le bas contrôlent la raquette.
Les flèches gauche et droite
contrôlent la vitesse de la
balle.""")

def a_propos():
    mbox.showinfo("À propos",
        """Ce code est distribué sous
licence GNU/GPL v3. Il n'y a pas
de copie du texte de la licence :
pure flemme de ma part !""")

# La fenêtre du jeu
fen = Tk()
# Le titre de la fenêtre
fen.title("En Jeu...")
fen.attributes('-fullscreen', True)
# La barre de menu
bar = Menu(fen)

# Le premier menu
menu_jeu = Menu(bar)
# Le menu qui contient 'Nouveau jeu' et 'Quitter'
menu_jeu.add_command(label="Nouveau jeu", command=jouer, underline=0, accelerator="Ctrl+J")
menu_jeu.add_command(label="Quitter", command=quitter, underline=0, accelerator="Ctrl+Q")
# On ajoute ce menu a la barre
bar.add_cascade(label="Jeu", menu=menu_jeu, underline=0)

# Le menu 'Aide', avec la regle et un 'À propos'
menu_aide = Menu(bar)
menu_aide.add_command(label="Règle du jeu", command=regle_du_jeu, underline=0)
menu_aide.add_command(label="À propos", command=a_propos, underline=2)
# On ajoute ce menu a la barre
bar.add_cascade(label="Aide", menu=menu_aide, underline=0)

# On ajoute la barre de menus a la fenêtre
fen.config(menu=bar)

# Le canevas dans lequel apparaîtront les dessins
can = Canvas(fen, bg="dark grey", height=HAUTEUR, width=LARGEUR)
can.pack()

# Les labels qui comptent succès et échecs
touche_sv = StringVar()
manque_sv = StringVar()

touche_sv.set("Touché : {}".format(config_params["balles_touchées"]))
manque_sv.set("Manqué : {}".format(config_params["balles_manquées"]))
Label(fen, textvariable=touche_sv).pack()
Label(fen, textvariable=manque_sv).pack()

# Les bindings entre touches et fonctions
fen.bind("<KeyPress>", enfoncer)
fen.bind("<KeyRelease>", relacher)
fen.bind("<Control-J>", jouer)
fen.bind("<Control-j>", jouer)
fen.bind("<Control-Q>", quitter)
fen.bind("<Control-q>", quitter)

# Boucle principale de la fenêtre
fen.mainloop()
