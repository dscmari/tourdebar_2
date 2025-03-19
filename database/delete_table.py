import sqlite3

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect("database.db")
cur = conn.cursor()

# Tabelle löschen
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("DROP TABLE IF EXISTS addresses")
cur.execute("DROP TABLE IF EXISTS bars")
cur.execute("DROP TABLE IF EXISTS tours")
cur.execute("DROP TABLE IF EXISTS stops")
cur.execute("DROP TABLE IF EXISTS tour_players")
cur.execute("DROP TABLE IF EXISTS games")
cur.execute("DROP TABLE IF EXISTS tour_games")

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()

print("Tabelle gelöscht.")
