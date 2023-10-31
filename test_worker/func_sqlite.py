import sqlite3
import os

def crear_tabla(cursor):
    #Crear una tabla para almacenar los datos
    cursor.execute('''CREATE TABLE Datos (
                  id INTEGER PRIMARY KEY,
                  Tiempo DATETIME,
                  Vibracion REAL,
                  Latitud TEXT,
                  Longitud TEXT,
                  Captura BLOB,
                  Anormal INTEGER
                  )''')
    return
    
def comprobar_tabla(cursor):
    #Hacer una consulta a la Base de Datos
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='Datos'")
    tabla = cursor.fetchone()
    
    #Si no existe tabla, devolver False
    if tabla:
        return True
    else:
        return False

def almacenar_datos(datos, bd):
    #Conectar o crear una base de datos
    conn = sqlite3.connect(bd)

    #Crear un objeto cursor
    cursor = conn.cursor()

    #Comprobar si la tabla existe
    if comprobar_tabla(cursor) == False:
        crear_tabla(cursor)
        
    #Obteniendo datos que se recibieron
    tiempo = datos["Tiempo"]
    vibracion = datos["Vibracion"]
    latitud = datos["Latitud"]
    longitud = datos["Longitud"]
    captura = datos["Captura"]
    
    #Comprobando anormalidad de la vibracion
    if (vibracion >= 1.5) and (vibracion <= 2.5):
        anormal = 1
    else:
        anormal = 0
    
    #Guardando datos haciendo un registro a la tabla
    cursor.execute("INSERT INTO Datos (Tiempo, Vibracion, Latitud, Longitud, Captura, Anormal) VALUES (?, ?, ?, ?, ?, ?)",
                   (tiempo, vibracion, latitud, longitud, captura, anormal))

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()
    return