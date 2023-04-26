import sqlite3

conn = sqlite3.connect('alumnosApp.db')

cursor = conn.cursor()

nombre = input("Ingrese el nombre a buscar: ")


res = cursor.fetchall()

if res:
    for resultado in res:
        print("ID:", resultado[0])
        print("Nombre:", resultado[1])
        print("Apellido:", resultado[2])
else:
    print("No se encontraron resultados.")

conn.close()
