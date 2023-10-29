import sqlite3
import cv2
import base64
import numpy as np

def base64_a_imagen(imagen_base64):
    try:
        # Decodificar la cadena base64 a bytes
        imagen_bytes = base64.b64decode(imagen_base64)

        # Convertir los bytes en un array de numpy
        np_arr = np.frombuffer(imagen_bytes, np.uint8)

        # Decodificar el array en una imagen OpenCV
        imagen = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        return imagen

    except Exception as e:
        print("Error al convertir la cadena a imagen:", e)
        return None

# Conectarse a la base de datos
conn = sqlite3.connect("basededatos.db")

# Crear un objeto cursor
cursor = conn.cursor()

# Realizar una consulta para recuperar datos
cursor.execute("SELECT * FROM Datos")

# Obtener los resultados de la consulta
resultados = cursor.fetchall()

# Procesar los resultados
for fila in resultados:
    id, tiempo,vibracion, latitud, longitud, captura, anormal = fila
    print(f"ID: {id}")
    print(f"Tiempo: {tiempo}")
    print(f"Vibración: {vibracion}")
    print(f"Latitud: {latitud}")
    print(f"Longitud: {longitud}")
    print(f"Anormal: {anormal}")
    print("\n\n")
    
    #Mostrar imagen
    imagen = base64_a_imagen(captura)

    if imagen is not None:
        # Mostrar la imagen
        cv2.imshow("Imagen desde base64", imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Cerrar la conexión
conn.close()
