# Spalten umbenennen

#ALTER TABLE table_name RENAME TO new_table_name;
#ALTER TABLE table_name RENAME COLUMN old_column_name TO new_column_name;
# Beispiel:
#cur.execute('ALTER TABLE players RENAME COLUMN old_column_name TO new_column_name')


# Bestehende Tabelle mit AUTO_INCREMENT-ID ändern:
# Erstelle eine neue Tabelle mit der gewünschten ID-Spalte,
# kopiere die Daten und lösche dann die alte Tabelle.
import sqlite3

try:
    conn = sqlite3.connect('database.db')
    print('Opened databank successfully')

    cur = conn.cursor()

    # Schritt 1: Erstelle eine neue Tabelle mit AUTOINCREMENT-ID (z.B. bars_new)
    cur.execute('''CREATE TABLE IF NOT EXISTS bars_new (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,  
                    name TEXT NOT NULL,
                    brewery TEXT NOT NULL,
                    street TEXT NOT NULL,
                    city TEXT NOT NULL
                )''')

    # Schritt 2: Daten von der alten Tabelle "bars" in die neue Tabelle "bars_new" kopieren
    cur.execute('''INSERT INTO bars_new (name, brewery, street, city)
                   SELECT name, brewery, street, city FROM bars''')

    # Schritt 3: Lösche die alte Tabelle "bars"
    cur.execute('DROP TABLE bars')

    # Schritt 4: Benenne die neue Tabelle "bars_new" in "bars" um
    cur.execute('ALTER TABLE bars_new RENAME TO bars')

    # Änderungen speichern und Verbindung schließen
    conn.commit()

except sqlite3.Error as e:
    print(f"Fehler bei der Datenbankoperation: {e}")

#testen, ob die Änderung erfolgt ist
try:
    conn = sqlite3.connect('database.db')
    print('Verbindung zur Datenbank erfolgreich hergestellt.')

    cur = conn.cursor()

    # Schritt 1: Zeige die Struktur der Tabelle "bars" an
    cur.execute("PRAGMA table_info(bars);")
    columns = cur.fetchall()

    print("Struktur der Tabelle 'bars':")
    for column in columns:
        print(f"Spaltenname: {column[1]}, Typ: {column[2]}, Ist es eine PRIMARY KEY Spalte: {column[5]}")

except sqlite3.Error as e:
    print(f"Fehler bei der Datenbankoperation: {e}")

finally:
    if conn:
        conn.close()
    print("Die ID wurde erfolgreich geändert und die Tabelle wurde aktualisiert.")

