import tkinter as tk
from tkinter import ttk
import random
import os

class LoadingScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Chargement...")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.root.attributes('-fullscreen', True)
        
        # Fond d'écran pour une ambiance de jeu
        self.background_image = tk.PhotoImage(file="background_image.png")
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Label pour afficher le texte "Chargement..."
        self.loading_label = tk.Label(root, text="Chargement en cours...", font=("Helvetica", 16), bg="black", fg="white")
        self.loading_label.pack(pady=20)

        # Label pour afficher les astuces
        self.tip_label = tk.Label(root, text="", font=("Helvetica", 12), bg="black", fg="white", anchor="sw", justify="left")
        self.tip_label.place(relx=0, rely=1, anchor="sw", x=10, y=-10)

        # Barre de progression pour le chargement
        self.progress_bar = ttk.Progressbar(root, orient='horizontal', length=300, mode='indeterminate', style='Custom.Horizontal.TProgressbar')
        self.progress_bar.place(relx=0.5, rely=0.5, anchor="center")
        self.progress_bar.start(10)  # Démarrer la barre de progression

        # Liste d'astuces
        self.tips = [
            {"title": "Astuce:", "text": "Vous pouvez faire CTRL + J pour commencer une partie, ou simplement accéder au menu rapide de la partie (il est nommé Jeu)"},
            {"title": "Astuce:", "text": "Cela est pratique de savoir quitter sans risquer de perdre sa progression, ou ses paramètres enregistrés, CTRL + Q peux fonctionner, mais rappeler vous que vous pouvez aussi quitter en accédant à la rubrique Jeu."},
            {"title": "Astuce:", "text": "Si vous rencontrez une erreur, informez-le nous ;D"},
            {"title": "Astuce:", "text": "Apprenez à viser les coins et les bords de l'écran pour que la balle rebondisse de manière imprévisible pour votre adversaire."},
            {"title": "Astuce:", "text": "Une bonne partie se fait avec des paramètres bien appliqués, alors jetez toujours un coup d'oeil à vos paramètres ;D"},
            {"title": "Astuce:", "text": "Essayez de frapper la balle à différentes vitesses pour déstabiliser votre adversaire et l'empêcher de s'adapter à un rythme constant."},
            {"title": "Astuce:", "text": "Expérimentez avec des effets comme le topspin et le backspin pour modifier la trajectoire de la balle et surprendre votre adversaire."},
            {"title": "Astuce:", "text": "Plus vous jouez, plus vous développerez vos réflexes et votre habileté. Consacrez du temps à l'entraînement pour améliorer vos compétences."},
            {"title": "Astuce:", "text": "Sa va trop vite ? Modifiez la vitesse ou la difficulté du jeu ;D"},
            {"title": "Astuce:", "text": "Vous pouvez vous déplacer en utilisant les flèches directionnelles :D"},
            {"title": "Astuce:", "text": "Un easter egg est présent dans le jeu !"},
            {"title": "Astuce:", "text": "Vous pouvez faire CTRL + J pour commencer une partie, ou simplement accéder au menu rapide de la partie (il est nommé Jeu)"},
        ]
        self.current_tip_index = -1

        # Associer la fonction show_next_tip à chaque touche pressée
        self.root.bind('<Key>', self.show_next_tip)

        # Afficher une astuce au démarrage
        self.show_next_tip(None)

        # Lancer le chargement du jeu
        self.load_game()

    def load_game(self):
        # Simulation de chargement - ici, vous pouvez ajouter les opérations de chargement réelles
        # Remplacer ce délai par le chargement réel du jeu
        self.root.after(4000, self.show_menu)

    def show_menu(self, event=None):
        self.root.after(100, self.root.destroy)
        # Lancer l'écran de menu principal
        # Remplacez cette ligne par le lancement de votre menu principal
        os.system("python play.py")
        # Après le chargement, aller vers menu.py
        # Mettez votre code pour naviguer vers menu.py ici
        # Détruire l'écran de chargement
        self.root.destroy()
    def show_next_tip(self, event):
        # Sélectionner une astuce aléatoire différente de l'astuce actuelle
        next_index = self.current_tip_index
        while next_index == self.current_tip_index:
            next_index = random.randint(0, len(self.tips) - 1)
        
        self.current_tip_index = next_index
        tip = self.tips[self.current_tip_index]

        # Mettre à jour le label avec le titre et le texte de l'astuce
        tip_text = f"{tip['title']}\n{tip['text']}"
        self.tip_label.config(text=tip_text)

def main():
    root = tk.Tk()
    style = ttk.Style(root)
    style.theme_use('clam')
    style.configure("Custom.Horizontal.TProgressbar", background='black', troughcolor='gray50', bordercolor='gray40', darkcolor='gray40', lightcolor='gray70')
    app = LoadingScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()