import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                value TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def insert_record(self, name, value):
        self.cursor.execute('''
            INSERT INTO records (name, value) VALUES (?, ?)
        ''', (name, value))
        self.connection.commit()

    def fetch_records(self):
        self.cursor.execute('SELECT * FROM records')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()