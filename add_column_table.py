#Wenn du eine Spalte zu einer bestehenden Tabelle hinzufügen möchtest,

import sqlite3

try:
    conn = sqlite3.connect('database.db')
    print('Opened databank successfully')

    cur = conn.cursor()

    # Spalte "age" zur Tabelle "players" hinzufügen
    cur.execute("ALTER TABLE players ADD COLUMN age INTEGER")

    # Änderungen speichern und Verbindung schließen
    conn.commit()

except sqlite3.Error as e:
    print(f"Fehler bei der Datenbankoperation: {e}")

finally:
    if conn:
        conn.close()
    print("Spalte wurde erfolgreich hinzugefügt.")