# Füge Daten in die Tabelle ein

import sqlite3

try:
    conn = sqlite3.connect('database.db')
    print('Verbindung zur Datenbank erfolgreich hergestellt.')

    cur = conn.cursor()

    # Schritt 1: Daten ohne ID in die Tabelle einfügen

    # users
    cur.execute("INSERT INTO users (username, password) VALUES ('Max Mustermann', 'frei')")

    # Zuerst die Adressen in die 'addresses' Tabelle einfügen
    cur.execute("INSERT INTO addresses (street, city, country) VALUES ('Zugspitzstraße 19', 'München','Germany')")
    address_id_1 = cur.lastrowid
    cur.execute("INSERT INTO addresses (street, city, country) VALUES ('Geyerstraße 17', 'München','Germany')")
    address_id_2 = cur.lastrowid
    cur.execute("INSERT INTO addresses (street, city, country) VALUES ('Reifenstuelstraße 9', 'München','Germany')")
    address_id_3 = cur.lastrowid

    # Bars mit den entsprechenden Adressen einfügen
    cur.execute("INSERT INTO bars (name, brewery, address_id) VALUES ('Bumsvoll', 'Frei', ?)", (address_id_1,))
    cur.execute("INSERT INTO bars (name, brewery, address_id) VALUES ('Geyerwally', 'Frei', ?)", (address_id_2,))
    cur.execute("INSERT INTO bars (name, brewery, address_id) VALUES ('Bierschuppen', 'Schweiger', ?)", (address_id_3,))


    #tours
    cur.execute("INSERT INTO tours (name) VALUES ('Paul heiratet')")


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