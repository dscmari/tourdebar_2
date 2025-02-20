# Füge Daten in die Tabelle ein

import sqlite3

try:
    conn = sqlite3.connect('database.db')
    print('Verbindung zur Datenbank erfolgreich hergestellt.')

    cur = conn.cursor()

    # Schritt 1: Daten ohne ID in die Tabelle einfügen
    cur.execute("INSERT INTO bars (name, brewery, street, city) VALUES ('Bumsvoll', 'frei', 'Zugspitzstrasse 19', 'München')")
    cur.execute("INSERT INTO bars (name, brewery, street, city) VALUES ('Geyerwally', 'Craft Beer', 'Geyerstraße', 'München')")
    cur.execute("INSERT INTO bars (name, brewery, street, city) VALUES ('Bierschuppen', 'Schweiger', 'Reifenstuelstraße 9', 'München')")

    # Änderungen speichern
    conn.commit()

    # Schritt 2: Alle Daten aus der Tabelle abfragen
    cur.execute("SELECT * FROM bars")
    rows = cur.fetchall()

    print("Alle Einträge in der 'bars'-Tabelle:")
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print(f"Fehler bei der Datenbankoperation: {e}")

finally:
    if conn:
        conn.close()