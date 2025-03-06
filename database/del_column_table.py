import sqlite3

try:
    conn = sqlite3.connect('database.db')
    print('Opened databank successfully')

    cur = conn.cursor()

    # Schritt 1: Neue Tabelle erstellen (ohne die 'age'-Spalte)
    cur.execute('''CREATE TABLE IF NOT EXISTS players_new (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    city TEXT NOT NULL
                )''')

    # Schritt 2: Daten von der alten Tabelle in die neue Tabelle kopieren
    cur.execute('''INSERT INTO players_new (id, name, city)
                   SELECT id, name, city FROM players''')

    # Schritt 3: Alte Tabelle löschen
    cur.execute('DROP TABLE players')

    # Schritt 4: Neue Tabelle umbenennen
    cur.execute('ALTER TABLE players_new RENAME TO players')

    # Änderungen speichern und Verbindung schließen
    conn.commit()

except sqlite3.Error as e:
    print(f"Fehler bei der Datenbankoperation: {e}")

finally:
    if conn:
        conn.close()
    print("Spalte erfolgreich gelöscht.")
