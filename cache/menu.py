import tkinter as tk
from tkinter import ttk
import os

class MenuPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu")
        self.root.attributes('-fullscreen', True)

        # Fond d'écran pour une ambiance de jeu
        self.background_image = tk.PhotoImage(file="background_image.png")
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Titre du jeu
        self.game_title = tk.Label(root, text="Jeu de Pong", font=("Helvetica", 24), bg="black", fg="white")
        self.game_title.pack(pady=50)

        # Boutons
        self.play_button = ttk.Button(root, text="JOUER", command=self.open_play_menu)
        self.play_button.pack(pady=20)

        self.settings_button = ttk.Button(root, text="PARAMETRES", command=self.open_settings)
        self.settings_button.pack(pady=20)

        self.quit_button = ttk.Button(root, text="QUITTER", command=self.quit_game)
        self.quit_button.pack(pady=20)

    def open_play_menu(self):
        self.root.after(100, self.root.destroy)  # Ferme la fenêtre principale après 100ms
        os.system("python menu_play.py")

    def open_settings(self):
        self.root.after(100, self.root.destroy)  # Ferme la fenêtre principale après 100ms
        os.system("python parametre.py")

    def quit_game(self):
        self.root.destroy()

def main():
    root = tk.Tk()
    style = ttk.Style(root)
    style.theme_use('clam')

    app = MenuPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
