import time
import random

# Coordenadas iniciales
latitud = 21.200642044259617
longitud = -86.8233056004058

# Velocidad del tren en metros por segundo
velocidad = 10.0  # 10 metros por segundo (ajusta según sea necesario)

# Dirección inicial (en grados, 0: Este, 90: Norte, 180: Oeste, 270: Sur)
direccion = 0

# Función para simular el movimiento del tren
def mover_tren():
    global latitud, longitud, direccion

    # Simula un cambio en la dirección (puedes ajustar esto)
    if random.random() < 0.1:  # Cambio de dirección con una probabilidad del 10%
        direccion = random.choice([0, 90, 180, 270])

    # Calcula el cambio en las coordenadas basado en la velocidad
    if direccion == 0:
        longitud += (velocidad / 100000)  # 100,000 metros en 1 grado de longitud aproximadamente
    elif direccion == 90:
        latitud += (velocidad / 100000)  # 100,000 metros en 1 grado de latitud aproximadamente
    elif direccion == 180:
        longitud -= (velocidad / 100000)
    elif direccion == 270:
        latitud -= (velocidad / 100000)

    print(f"Latitud: {latitud}, Longitud: {longitud}")

    time.sleep(1)  # Tiempo de espera para simular el movimiento

if __name__ == "__main__":
    try:
        while True:
            mover_tren()
    except KeyboardInterrupt:
        print("Simulacion Terminada")