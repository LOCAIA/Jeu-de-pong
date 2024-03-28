import tkinter as tk
from tkinter import ttk
import os

class MenuPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu")
        self.root.attributes('-fullscreen', True)

        # Chargement des paramètres depuis le fichier texte
        self.load_settings()

        # Fond d'écran pour une ambiance de jeu
        self.background_image = tk.PhotoImage(file="background_image.png")
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Titre du jeu
        self.game_title = tk.Label(root, text="Jeu de Pong", font=("Helvetica", 24), bg="black", fg="white")
        self.game_title.pack(pady=50)

        # Langue
        self.language_label = tk.Label(root, text="Langue:")
        self.language_label.pack()
        self.language_var = tk.StringVar(value=self.settings['Parametres']['Langue'])
        self.language_entry = ttk.Combobox(root, textvariable=self.language_var, state='readonly', values=["Français", "Anglais", "Espagnol"])
        self.language_entry.pack()

        # Volume Sonore
        self.volume_label = tk.Label(root, text="Vitesse de la balle (%):")
        self.volume_label.pack()
        self.volume_var = tk.StringVar(value=self.settings['Parametres']['VolumeSonPourcent'])
        self.volume_entry = ttk.Combobox(root, textvariable=self.volume_var, state='readonly', values=["0", "5", "10", "15", "20", "25", "30", "35", "40", "45", "55", "60", "65", "70", "75", "80", "85", "90", "95", "100"])
        self.volume_entry.pack()

        # Sensibilité de la Souris
        self.sensitivity_label = tk.Label(root, text="Sensibilité de la Souris (%):")
        self.sensitivity_label.pack()
        self.sensitivity_var = tk.StringVar(value=self.settings['Parametres']['SensibiliteSourisPourcent'])
        self.sensitivity_entry = ttk.Combobox(root, textvariable=self.sensitivity_var, state='readonly', values=["0", "5", "10", "15", "20", "25", "30", "35", "40", "45", "55", "60", "65", "70", "75", "80", "85", "90", "95", "100"])
        self.sensitivity_entry.pack()

        # Sauvegarde Automatique
        self.autosave_label = tk.Label(root, text="Sauvegarde Automatique:")
        self.autosave_label.pack()
        self.autosave_var = tk.StringVar(value=self.settings['Sauvegarde']['SauvegardeAutomatiqueOuiNon'])
        self.autosave_entry = ttk.Combobox(root, textvariable=self.autosave_var, state='readonly', values=["Oui", "Non"])
        self.autosave_entry.pack()

        # Boutons pour l'assignation des touches de contrôle
        self.controls_label = tk.Label(root, text="Assignation des touches de contrôle:")
        self.controls_label.pack()
        self.move_button = ttk.Button(root, text="Déplacer Personnage", command=self.assign_move_key)
        self.move_button.pack()
        self.action_button = ttk.Button(root, text="Actions sur Personnage", command=self.assign_action_key)
        self.action_button.pack()
        self.menu_button = ttk.Button(root, text="Ouvrir Menu", command=self.assign_menu_key)
        self.menu_button.pack()

        # Boutons
        self.save_button = ttk.Button(root, text="Enregistrer", command=self.save_settings)
        self.save_button.pack(pady=20)

        self.quit_button = ttk.Button(root, text="RETOURS", command=self.back)
        self.quit_button.pack(pady=20)

    def load_settings(self):
        # Chargement des paramètres depuis le fichier texte
        with open('parametre.txt', 'r') as file:
            self.settings = {}
            current_section = ""
            for line in file:
                line = line.strip()
                if line.startswith('[') and line.endswith(']'):
                    current_section = line[1:-1]
                    self.settings[current_section] = {}
                elif '=' in line:
                    key, value = line.split('=')
                    self.settings[current_section][key.strip()] = value.strip()

    def save_settings(self):
        # Sauvegarde des paramètres dans le fichier texte
        self.settings['Parametres']['Langue'] = self.language_var.get()
        self.settings['Parametres']['VolumeSonPourcent'] = self.volume_var.get()
        self.settings['Parametres']['SensibiliteSourisPourcent'] = self.sensitivity_var.get()
        self.settings['Sauvegarde']['SauvegardeAutomatiqueOuiNon'] = self.autosave_var.get()

        with open('parametre.txt', 'w') as file:
            for section, options in self.settings.items():
                file.write(f"[{section}]\n")
                for key, value in options.items():
                    file.write(f"{key}={value}\n")

    def back(self):
        # Retour à la page précédente
        self.root.after(100, self.root.destroy)  # Ferme la fenêtre principale après 100ms
        os.system("python menu.py")

    def assign_move_key(self):
        # Code pour assigner la touche de déplacement du personnage
        pass

    def assign_action_key(self):
        # Code pour assigner la touche d'action sur le personnage
        pass

    def assign_menu_key(self):
        # Code pour assigner la touche d'ouverture du menu
        pass

def main():
    root = tk.Tk()
    style = ttk.Style(root)
    style.theme_use('clam')

    app = MenuPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()