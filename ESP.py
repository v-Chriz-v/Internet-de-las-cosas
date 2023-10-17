import time
from datetime import datetime
import json
from SensorVibracion import SensorVibracion

class ESP:
    def __init__(self):
        self.sensor = SensorVibracion()

    def simular_sensor(self, duracion_segundos, archivo_json):
        start_time = datetime.now()
        registros = []

        while (datetime.now() - start_time).total_seconds() < duracion_segundos:
            valor_vibracion = self.sensor.generar_valor_vibracion()
            current_time = datetime.now()
            registro = {"Tiempo": str(current_time), "Vibracion": valor_vibracion}
            registros.append(registro)

            print(f"Tiempo: {current_time}, Vibracion: {valor_vibracion}")

            time.sleep(1.0)

        # Guarda los registros en un archivo JSON
        with open(archivo_json, 'w') as json_file:
            json.dump(registros, json_file, indent=4)

if __name__ == "__main__":
    esp = ESP()
    duracion_captura = 10  # Duración de la captura en segundos
    archivo_json = "data/registros.json"  # Nombre del archivo JSON
    esp.simular_sensor(duracion_captura, archivo_json)
