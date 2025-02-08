import tkinter as tk
from tkinter import ttk
from methods import Methods
from database import Database

class InterfaceGraphique:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gestion des notes")
        self.root.geometry("750x400")
        self.methods = Methods(self)
        self.db = Database()
        self.db.creer_table()

        # Variables pour les menus déroulants
        self.concentration_var = tk.StringVar(value="Bonne")
        self.attitude_var = tk.StringVar(value="Bonne")
        self.sexe_var = tk.StringVar(value="Masculin")

        self.creer_widgets()

    def creer_widgets(self):
        # Cadre pour les champs de saisie
        cadre_saisie = tk.Frame(self.root)
        cadre_saisie.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        # Prénom
        tk.Label(cadre_saisie, text="Prénom:").grid(row=0, column=0, padx=5, sticky="w")
        self.entry_prenom = tk.Entry(cadre_saisie, width=20)
        self.entry_prenom.grid(row=0, column=1, padx=5)

        # Sexe
        tk.Label(cadre_saisie, text="Sexe:").grid(row=0, column=2, padx=5, sticky="w")
        ttk.Combobox(cadre_saisie, textvariable=self.sexe_var, 
                    values=["Masculin", "Féminin"], state="readonly").grid(row=0, column=3, padx=5)

        # Note
        tk.Label(cadre_saisie, text="Note:").grid(row=0, column=4, padx=5, sticky="w")
        self.entry_note = tk.Entry(cadre_saisie, width=10)
        self.entry_note.grid(row=0, column=5, padx=5)

        # Concentration
        tk.Label(cadre_saisie, text="Concentration:").grid(row=1, column=0, padx=5, sticky="w")
        ttk.Combobox(cadre_saisie, textvariable=self.concentration_var,
                    values=["Bonne", "Moyenne", "Mauvaise"], state="readonly").grid(row=1, column=1, padx=5)

        # Attitude
        tk.Label(cadre_saisie, text="Attitude:").grid(row=1, column=2, padx=5, sticky="w")
        ttk.Combobox(cadre_saisie, textvariable=self.attitude_var,
                    values=["Bonne", "Moyenne", "Agitée"], state="readonly").grid(row=1, column=3, padx=5)

        # Bouton Valider
        tk.Button(self.root, text="Valider", command=self.methods.afficher_commentaire)\
            .grid(row=2, column=0, columnspan=4, pady=10, sticky="ew")

        # Zone de résultat avec ascenseur
        cadre_resultat = tk.Frame(self.root, bd=2, relief="solid")
        cadre_resultat.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        self.text_resultat = tk.Text(cadre_resultat, height=10, wrap=tk.WORD, state=tk.DISABLED)
        scrollbar = tk.Scrollbar(cadre_resultat, command=self.text_resultat.yview)
        self.text_resultat.configure(yscrollcommand=scrollbar.set)
        
        self.text_resultat.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y")

        # Boutons
        cadre_boutons = tk.Frame(self.root)
        cadre_boutons.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        
        boutons = [
            ("Copier", self.methods.copier_commentaire),
            ("Effacer", self.methods.effacer_tout),
            ("Enregistrer", self.methods.enregistrer_donnees),
            ("Quitter", self.root.quit)
        ]
        
        for text, cmd in boutons:
            tk.Button(cadre_boutons, text=text, command=cmd)\
                .pack(side="left", padx=5, expand=True, fill="x")

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(3, weight=1)

    def run(self):
        self.root.mainloop()