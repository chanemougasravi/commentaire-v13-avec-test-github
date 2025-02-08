import sqlite3
import os

class Database:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.conn = sqlite3.connect(os.path.join(base_dir, "eleves.db"))
        self.cursor = self.conn.cursor()
        self.creer_table()

    def creer_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS eleves (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                prenom TEXT NOT NULL,
                sexe TEXT NOT NULL,
                note REAL NOT NULL,
                concentration TEXT NOT NULL,
                attitude TEXT NOT NULL,
                commentaire TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def enregistrer_eleve(self, prenom, sexe, note, concentration, attitude, commentaire):
        self.cursor.execute("""
            INSERT INTO eleves (prenom, sexe, note, concentration, attitude, commentaire)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (prenom, sexe, note, concentration, attitude, commentaire))
        self.conn.commit()

    def __del__(self):
        self.conn.close()