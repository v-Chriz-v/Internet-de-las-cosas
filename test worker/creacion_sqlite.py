import sqlite3
import os

database_name = "mi_base_de_datos.db"

# 1. Conectar o crear una base de datos
conn = sqlite3.connect(database_name)

# 2. Crear un objeto cursor
cursor = conn.cursor()

# 3. Crear una tabla para almacenar los datos
cursor.execute('''CREATE TABLE Datos (
              id INTEGER PRIMARY KEY,
              Tiempo DATETIME,
              Ubicacion TEXT,
              Vibracion REAL,
              Captura BLOB
              )''')

# 4. Insertar datos en la tabla
tiempo = "2023-10-25 15:30:00"  # Ejemplo de fecha y hora
ubicacion = "Latitud: 123.456, Longitud: -78.901"  # Ejemplo de ubicación
vibracion = 0.123  # Ejemplo de valor de vibración
# Ejemplo de captura de imagen en formato binario (debes adaptar esta parte a tu caso)
with open("image.png", "rb") as imagen_file:
    captura = imagen_file.read()

# Insertar un registro en la tabla
cursor.execute("INSERT INTO Datos (Tiempo, Ubicacion, Vibracion, Captura) VALUES (?, ?, ?, ?)",
               (tiempo, ubicacion, vibracion, captura))

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()
