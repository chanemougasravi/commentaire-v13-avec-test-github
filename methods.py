import tkinter as tk
from tkinter import messagebox
import requests

class Methods: # toutes les methods dans ce fichier
    def __init__(self, ui):
        self.ui = ui
        self.api_key = "sk-5e4336b43d104960aa865b9941d3948d"
        self.api_url = "https://api.deepseek.com/v1/chat/completions"

    def generate_comment_with_deepseek(self, input_text):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "Générez un commentaire scolaire en français."},
                {"role": "user", "content": input_text}
            ],
            "max_tokens": 200,
            "temperature": 0.7
        }

        try:
            response = requests.post(self.api_url, headers=headers, json=data)
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            messagebox.showerror("Erreur", f"Code {response.status_code}: {response.text}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec de connexion: {str(e)}")
        return None

    def afficher_commentaire(self):
        prenom = self.ui.entry_prenom.get()
        note = self.ui.entry_note.get()
        sexe = self.ui.sexe_var.get()
        concentration = self.ui.concentration_var.get()
        attitude = self.ui.attitude_var.get()

        if not all([prenom, note]):
            messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs obligatoires")
            return

        try:
            note = float(note)
            if not (0 <= note <= 20):
                raise ValueError
        except ValueError:
            messagebox.showerror("Erreur", "Note invalide (doit être entre 0 et 20)")
            return

        input_text = f"Élève {prenom} ({sexe}) - Note: {note}/20\n"
        input_text += f"Concentration: {concentration}, Attitude: {attitude}\n"
        input_text += "Générer un commentaire constructif de 5 lignes maximum."

        commentaire = self.generate_comment_with_deepseek(input_text)
        
        self.ui.text_resultat.config(state=tk.NORMAL)
        self.ui.text_resultat.delete(1.0, tk.END)
        self.ui.text_resultat.insert(tk.END, commentaire or "Échec de génération")
        self.ui.text_resultat.config(state=tk.DISABLED)

    def effacer_tout(self):
        self.ui.entry_prenom.delete(0, tk.END)
        self.ui.entry_note.delete(0, tk.END)
        self.ui.sexe_var.set("Masculin")
        self.ui.concentration_var.set("Bonne")
        self.ui.attitude_var.set("Bonne")
        self.ui.text_resultat.config(state=tk.NORMAL)
        self.ui.text_resultat.delete(1.0, tk.END)
        self.ui.text_resultat.config(state=tk.DISABLED)

    # Les méthodes copier_commentaire et enregistrer_donnees restent similaires
    # ... (adaptez-les selon le même modèle)
    def copier_commentaire(self):
        """
        Copy the generated comment to the clipboard.
        """
        commentaire = self.ui.text_resultat.get(1.0, tk.END).strip()
        if commentaire:
            self.ui.root.clipboard_clear()
            self.ui.root.clipboard_append(commentaire)
            messagebox.showinfo("Copié", "Le commentaire a été copié dans le presse-papiers.")
        else:
            messagebox.showwarning("Avertissement", "Aucun commentaire à copier.")

    def enregistrer_donnees(self):
        """
        Save the student's data to the database.
        """
        prenom = self.ui.entry_prenom.get()
        sexe = self.ui.sexe_var.get()  # Récupérer le sexe de l'élève
        note = self.ui.entry_note.get()
        commentaire = self.ui.text_resultat.get(1.0, tk.END).strip()
        concentration = self.ui.concentration_var.get()
        agitation = self.ui.agitation_var.get()

        if not prenom or not note or not commentaire:
            messagebox.showwarning("Avertissement", "Veuillez remplir tous les champs.")
            return

        try:
            note = float(note)
            if note < 0 or note > 20:
                messagebox.showwarning("Avertissement", "La note doit être comprise entre 0 et 20.")
                return
        except ValueError:
            messagebox.showwarning("Avertissement", "La note doit être un nombre valide.")
            return

        # Enregistrer dans la base de données
        self.ui.db.enregistrer_eleve(prenom, sexe, note, commentaire, concentration, agitation)
        messagebox.showinfo("Succès", "Les données ont été enregistrées avec succès.")