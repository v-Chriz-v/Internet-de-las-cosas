#Simulacion de un GPS
import random
import time

print("Iniciando simuacion de GPS...")

try:
    while True:
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)
        print(f"Latitud: {latitude}, Longitud: {longitude}")
        time.sleep(1)  # Emula la actualización periódica del GPS
except KeyboardInterrupt:
    print("Simulacion de GPS finalizada")