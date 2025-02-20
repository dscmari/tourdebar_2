import sqlite3

#Verbindung zur Datenbank aufbauen
conn = sqlite3.connect('database.db')
print('Opened databank was successfully')

#Curser für Datenbank erstellen, ein Cursor in SQLite ist notwendig,
# um SQL-Abfragen an die Datenbank zu senden und die Ergebnisse abzurufe
cur = conn.cursor()

# Tabelle "players" erstellen, falls sie nicht existiert
#cur.execute('''CREATE TABLE IF NOT EXISTS players(
#               id INTEGER PRIMARY KEY AUTOINCREMENT,
#               name TEXT NOT NULL,
#               age INTEGER NOT NULL,
#               city TEXT NOT NULL
#           )''')

# Tabelle "bars" erstellen, falls sie nicht existiert
cur.execute('''CREATE TABLE IF NOT EXISTS bars(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                brewery TEXT NOT NULL,
                street TEXT NOT NULL,
                city TEXT NOT NULL
            )''')


# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()

print("Datenbank und Tabelle wurden erfolgreich erstellt.")