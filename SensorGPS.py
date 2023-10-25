import random

class SensorGPS:
    def __init__(self):
        pass

    def generar_coordenadas(self):
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)
        return latitude, longitude
