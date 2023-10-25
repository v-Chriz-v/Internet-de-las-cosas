import time
from datetime import datetime
import json
from SensorVibracion import SensorVibracion
from SensorGPS import SensorGPS
import pika

class ESP:
    def __init__(self):
        self.sensor_vibracion = SensorVibracion()
        self.sensor_GPS = SensorGPS()

    def simular_sensores(self, duracion_segundos, archivo_json):
        start_time = datetime.now()
        registros = []

        while (datetime.now() - start_time).total_seconds() < duracion_segundos:
            valor_vibracion = self.sensor_vibracion.generar_valor_vibracion()
            latitud, longitud = self.sensor_GPS.generar_coordenadas()
            current_time = datetime.now()                                                                                                           
            registro = {"Tiempo": str(current_time), "Vibracion": valor_vibracion, "Latitud": latitud, "Longitud": longitud}
            registros.append(registro)

            print(f"Tiempo: {current_time}, Vibracion: {valor_vibracion}, Latitud {latitud} Longitud {longitud}")

            time.sleep(1.0)
        
        self.guardar_informacion(registros)

    def guardar_informacion(self, registros):
        # Guarda los registros en un archivo JSON
        with open(archivo_json, 'w') as json_file:
            json.dump(registros, json_file, indent=4)
    
    def publicar_informacion(self, archivo_json):
        try:
            # Establece la conexión con el servidor RabbitMQ
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            channel = connection.channel()

            # Declara una cola en RabbitMQ
            channel.queue_declare(queue='datos_sensores')

            # Lee el archivo JSON y publica su contenido en la cola
            with open(archivo_json, 'r') as json_file:
                data = json.load(json_file)
                for registro in data:
                    message = json.dumps(registro)
                    channel.basic_publish(exchange='', routing_key='datos_sensores', body=message)

            print("Los datos han sido publicados en la cola RabbitMQ.")

        except Exception as e:
            print(f"Error al publicar los datos: {e}")
        
        finally:
            #Cierra la conexion
            connection.close()

if __name__ == "__main__":
    esp = ESP()
    duracion_captura = 10  # Duración de la captura en segundos
    archivo_json = "dataESP/registros.json"  # Nombre del archivo JSON
    esp.simular_sensores(duracion_captura, archivo_json)
    esp.publicar_informacion(archivo_json)
