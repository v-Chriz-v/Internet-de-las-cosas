import random
import time

def simular_sensor_vibracion():

    while True:

        if random.random() < 0.8:
            valor_vibracion = random.uniform(0, 1.0)

        else:
            valor_vibracion = random.uniform(1.5, 2.5)

        print(f"Vibración: {valor_vibracion}")

        time.sleep(0.5)

if __name__ == "__main__":
    simular_sensor_vibracion()