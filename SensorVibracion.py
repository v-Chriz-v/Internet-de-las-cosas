import random

class SensorVibracion:
    def __init__(self):
        pass

    def generar_valor_vibracion(self):
        if random.random() < 0.8:
            valor_vibracion = random.uniform(0, 1.0)
        else:
            valor_vibracion = random.uniform(1.5, 2.5)
        return valor_vibracion
