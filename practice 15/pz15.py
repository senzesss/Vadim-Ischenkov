import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS lek_sredstva (
    kod INTEGER PRIMARY KEY,
    use TEXT NOT NULL,
    count INTEGER,
    price FLOAT NOT NULL,
    COUNTRY TEXT
)
''')


cursor.execute("INSERT OR IGNORE INTO lek_sredstva (kod, use, count, price, COUNTRY) VALUES (1, 'Парацетамол', 50, 150.0, 'Россия')")
cursor.execute("INSERT OR IGNORE INTO lek_sredstva (kod, use, count, price, COUNTRY) VALUES (2, 'Нурофен', 30, 300.5, 'Германия')")
cursor.execute("INSERT OR IGNORE INTO lek_sredstva (kod, use, count, price, COUNTRY) VALUES (3, 'ТРЕНБАЛОН', 100, 75.25, 'США')")



cursor.execute("SELECT * FROM lek_sredstva")
rows = cursor.fetchall()
print("\n1. Все записи:")
for row in rows:
    print(row)


cursor.execute("INSERT INTO lek_sredstva (kod, use, count, price, COUNTRY) VALUES (4, 'Ибупрофен', 40, 200.0, 'Франция')")
connection.commit()

cursor.execute("SELECT * FROM lek_sredstva WHERE count > 30")
rows = cursor.fetchall()
print("\n2. Записи, где count > 30:")
for row in rows:
    print(row)

cursor.execute("UPDATE lek_sredstva SET price = 175.0 WHERE kod = 1")
connection.commit()

cursor.execute("SELECT * FROM lek_sredstva WHERE COUNTRY = 'Россия'")
rows = cursor.fetchall()
print("\n3. Записи из России:")
for row in rows:
    print(row)


cursor.execute("DELETE FROM lek_sredstva WHERE kod = 3")
connection.commit()


cursor.execute("DELETE FROM lek_sredstva WHERE count < 40")
connection.commit()

cursor.execute("DELETE FROM lek_sredstva WHERE COUNTRY = 'Франция'")
connection.commit()


cursor.execute("SELECT * FROM lek_sredstva")
rows = cursor.fetchall()
print("\nФинальные данные:")
for row in rows:
    print(row) 
