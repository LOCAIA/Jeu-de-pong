# Pong Game

Ce projet consiste en une recréation du jeu classique Pong en utilisant Python et la bibliothèque Tkinter pour l'interface graphique.

## Introduction

Pong est l'un des premiers jeux vidéo d'arcade, créé en 1972 par Allan Alcorn. Il s'agit d'un jeu de sport virtuel simulant un match de tennis de table. Les joueurs déplacent des raquettes verticales sur les côtés de l'écran pour frapper une balle et la renvoyer à leur adversaire. Le but est de marquer des points en forçant l'adversaire à manquer la balle.

## Fonctionnalités

- Interface graphique simple utilisant Tkinter.
- Contrôles simples : déplacement des raquettes à l'aide des touches fléchées ou des touches W et S.
- Animation de la balle et rebondissement sur les bords et les raquettes.
- Comptage des points pour suivre le score des joueurs.
- Possibilité de démarrer une nouvelle partie ou de quitter le jeu.

## Comment jouer

1. Assurez-vous d'avoir Python installé sur votre système.
2. Clonez ce dépôt dans votre répertoire local.
3. Naviguez jusqu'au répertoire du jeu.
4. Lancez le jeu en exécutant le raccourci `Pong`.
5. Utilisez les touches fléchées pour déplacer votre raquette vers le haut ou vers le bas.
6. Essayez de renvoyer la balle à votre adversaire tout en évitant de manquer la balle.
7. Marquez des points en forçant votre adversaire à manquer la balle pour gagner la partie.

## Auteur

Ce jeu a été développé par Léo dans le cadre d'un projet personnel (en fait, je me faisais juste chier).


## Remerciements

- Merci à... Attends... Personne ne m'a aidé, alors pourquoi je ferais des remerciements ?



## Le code
Je suis cool, alors je vous donne un extrait de code pour faire un cercle qui se déplace dans une fenêtre ;D
```python
# coding: utf8
from tkinter import *
from datetime import datetime

DEBUG = False
touches = set()

def enfoncer(evt):
    """Ajoute une touche à l'ensemble des touches enfoncées"""
    touches.add(evt.keysym)
    if DEBUG:
        print("Pression :", touches)

def relacher(evt):
    """Enlève une touche à l'ensemble des touches enfoncées"""
    if evt.keysym in touches:
        touches.remove(evt.keysym)
    if DEBUG:
        print("Relâchement :", touches)

def action():
    """Gère les déplacements"""
    #if DEBUG:
    #    print(datetime.now())
    if "Left" in touches:
        c.move(r, -20, 0)   # Décalage vers la gauche (∆x = -20, ∆y = 0).
    if "Right" in touches:
        c.move(r, 20, 0)    # Décalage vers la droite (∆x = +20, ∆y = 0).
    if "Up" in touches:
        c.move(r, 0, -20)   # Décalage vers le haut (∆x = 0, ∆y = -20).
    if "Down" in touches:   # ⚠ l'axe des ordonnées est orienté VERS LE BAS !
        c.move(r, 0, 20)    # Décalage vers le bas  (∆x = 0, ∆y = +20).
    f.after(25, action)     # action() est exécutée toutes les 25 ms

f = Tk()
c = Canvas(f, bg='dark grey', width=800, height=600)
r = c.create_oval(350, 350, 450, 450, fill="red", width=10, outline="blue")
c.pack()
action()                    # action() est appelée une première fois

f.bind('<KeyPress>', enfoncer)      # enfoncer() est lancée par un appui sur N'IMPORTE QUELLE touche
f.bind('<KeyRelease>', relacher)    # relacher() est lancée lorsqu'on relâche N'IMPORTE QUELLE touche

f.mainloop()
```
