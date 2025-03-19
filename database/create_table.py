import sqlite3

#Verbindung zur Datenbank aufbauen
conn = sqlite3.connect('database.db')
print('Opened databank was successfully')

#Curser für Datenbank erstellen, ein Cursor in SQLite ist notwendig,
# um SQL-Abfragen an die Datenbank zu senden und die Ergebnisse abzurufe
cur = conn.cursor()

#Tabelle "users" erstellen, falls sie nicht existiert. Die Tabelle users speichert die
# Benutzerinformationen (id, username, password). Der Primärschlüssel ist id
cur.execute('''CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,          
                username VARCHAR(50) NOT NULL,
                password TEXT NOT NULL
           )''')

#Tabelle "adresses" erstellen, falls sie nicht existiert. Diese Tabelle speichert Adressinformationen (id, street, city, country).
# Die Tabelle bars verweist auf addresses durch den Fremdschlüssel address_id
cur.execute('''CREATE TABLE IF NOT EXISTS addresses(
                id INTEGER PRIMARY KEY AUTOINCREMENT,          
                street VARCHAR(100) NOT NULL,
                city VARCHAR(100) NOT NULL,
                country VARCHAR(100) NOT NULL
           )''')

# Tabelle "bars" erstellen, falls sie nicht existiert. Die Tabelle bars speichert
# Informationen zu Bars (id, name, address_id).
# Der Fremdschlüssel address_id verweist auf die Tabelle addresses.Durch den Fremdschlüssel
# (FOREIGN KEY) mit NOT NULL wird sichergestellt, dass jede Bar nur eine gültige
# Adresse haben kann.
cur.execute('''CREATE TABLE IF NOT EXISTS bars (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50) NOT NULL,
                brewery VARCHAR(50) NOT NULL,
                address_id INT NOT NULL,
                FOREIGN KEY (address_id) REFERENCES addresses(id) ON DELETE CASCADE
            )''')

#Die Tabelle tours speichert Tourinformationen (id, name). Weitere Tabellen, wie stops,
# tour_players und tour_games, verknüpfen sich über den Fremdschlüssel tour_id
cur.execute('''CREATE TABLE IF NOT EXISTS tours(
                id INTEGER PRIMARY KEY AUTOINCREMENT,          
                name VARCHAR(50) NOT NULL
           )''')

#Diese Tabelle speichert Stopps einer Tour (id, bar_id, tour_id, position).
# bar_id verweist auf die Tabelle bars und tour_id verweist auf die Tabelle tours.
cur.execute('''CREATE TABLE IF NOT EXISTS stops(
                id INTEGER PRIMARY KEY AUTOINCREMENT,          
                bar_id INTEGER,
                tour_id INTEGER,
                position INTEGER NOT NULL,
                FOREIGN KEY (bar_id) REFERENCES bars(id),
                FOREIGN KEY (tour_id) REFERENCES tours(id)
           )''')

#Die Tabelle tour_players speichert, welche Benutzer zu welcher
#Tour gehören (id, tour_id, user_id).Sie verbindet die Tabellen tours und users
# über Fremdschlüssel.
cur.execute('''CREATE TABLE IF NOT EXISTS tour_players(
                id INTEGER PRIMARY KEY AUTOINCREMENT,          
                tour_id INTEGER,
                user_id INTEGER,
                FOREIGN KEY (tour_id) REFERENCES tours(id),
                FOREIGN KEY (user_id) REFERENCES users(id)
           )''')

#Die Tabelle games speichert Spielinformationen (id, name, description).
cur.execute('''CREATE TABLE IF NOT EXISTS games(
                id INTEGER PRIMARY KEY AUTOINCREMENT,          
                name VARCHAR(50) NOT NULL,
                description TEXT NOT NULL
           )''')

#Diese Tabelle verbindet Touren mit den Spielen, die sie enthalten
#(id, tour_id, game_id). Sie verknüpft tours und games über Fremdschlüssel.
cur.execute('''CREATE TABLE IF NOT EXISTS tour_games(
                id INTEGER PRIMARY KEY AUTOINCREMENT,          
                tour_id INTEGER,
                game_id INTEGER,
                FOREIGN KEY (tour_id) REFERENCES tours(id),
                FOREIGN KEY (game_id) REFERENCES games(id)
           )''')

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()

print("Datenbank und Tabelle wurden erfolgreich erstellt.")

'''Primärschlüssel (PK): Jede Tabelle hat einen eindeutigen Primärschlüssel (id), 
um Datensätze eindeutig zu identifizieren.
Fremdschlüssel (FK): Tabellen wie bars, stops, tour_players, und tour_games verknüpfen 
sich mit anderen Tabellen (z.B. addresses, tours, users, games) durch Fremdschlüssel, 
um die referentielle Integrität sicherzustellen. Beispielsweise kann man in der 
stops-Tabelle nur gültige bar_id und tour_id Werte eintragen, die in den entsprechenden 
Tabellen existieren.'''