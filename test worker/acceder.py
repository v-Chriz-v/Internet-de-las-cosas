import sqlite3
from PIL import Image

# Conectarse a la base de datos
conn = sqlite3.connect("mi_base_de_datos.db")

# Crear un objeto cursor
cursor = conn.cursor()

# Realizar una consulta para recuperar datos
cursor.execute("SELECT * FROM Datos")

# Obtener los resultados de la consulta
resultados = cursor.fetchall()

# Procesar los resultados
for fila in resultados:
    id, tiempo, ubicacion, vibracion, captura = fila
    print(f"ID: {id}")
    print(f"Tiempo: {tiempo}")
    print(f"Ubicación: {ubicacion}")
    print(f"Vibración: {vibracion}")
    # Guardar el BLOB en un archivo
    nombre_archivo = "imagen_recuperada.png"
    with open(nombre_archivo, "wb") as archivo_salida:
        archivo_salida.write(captura)
    imagen = Image.open(nombre_archivo)
    imagen.show()
# Cerrar la conexión
conn.close()
