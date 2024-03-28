import tkinter as tk
from tkinter import ttk
import os
import winsound
class LoadingScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Veuillez patienter...")
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

        # Barre de progression pour le chargement
        self.progress_bar = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate', style='Custom.Horizontal.TProgressbar')
        self.progress_bar.place(relx=0.5, rely=0.5, anchor="center")
        
        # Lancer le chargement du jeu
        self.load_game()

    def load_game(self):
        # Liste de tuples (temps, pourcentage) pour définir le comportement de la barre de progression
        progress_steps = [
            (1000, 1),    # 1 seconde après : 1%
            (2500, 7),    # 2.5 secondes après : 7%
            (1000, 8),    # 1 seconde après : 8%
            (1000, 9),    # 1 seconde après : 9%
            (1000, 27),   # 1 seconde après : 27%
            (4000, 59),   # 4 secondes après : 59%
            (3000, 66),   # 3 secondes après : 66%
            (2000, 67),   # 2 secondes après : 67%
            (1000, 68),   # 1 seconde après : 68%
            (2000, 89),   # 2 secondes après : 89%
            (1000, 100)   # 1 seconde après : 100%
        ]

        # Fonction récursive pour mettre à jour la barre de progression avec les valeurs de progress_steps
        def update_progress(progress_index):
            if progress_index < len(progress_steps):
                time, percentage = progress_steps[progress_index]
                self.progress_bar['value'] = percentage
                self.root.after(time, update_progress, progress_index + 1)
            else:
                # Une fois que toutes les étapes sont terminées, lancer l'écran du menu principal
                self.show_menu()

        # Démarrer la mise à jour de la barre de progression avec la première étape
        update_progress(0)

    def show_menu(self):
        self.root.after(100, self.root.destroy)
        # Lancer l'écran de menu principal
        # Remplacez cette ligne par le lancement de votre menu principal
        os.system("python menu.py")
        # Après le chargement, aller vers menu.py
        # Mettez votre code pour naviguer vers menu.py ici
        # Détruire l'écran de chargement
        self.root.destroy()

def play_audio(file_path, loop=True):
    while True:
        winsound.PlaySound(file_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
        if not loop:
            break
        time.sleep(winsound.PlaySound(None, winsound.SND_FILENAME | winsound.SND_ASYNC))

def main():
    root = tk.Tk()
    style = ttk.Style(root)
    style.theme_use('clam')
    style.configure("Custom.Horizontal.TProgressbar", background='black', troughcolor='gray50', bordercolor='gray40', darkcolor='gray40', lightcolor='gray70')
    app = LoadingScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    audio_file = "maintheme.mp3"
    if os.path.exists(audio_file):
        play_audio(audio_file)
