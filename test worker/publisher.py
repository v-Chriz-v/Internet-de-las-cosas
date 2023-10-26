import pika
import json

class Publisher:
    def __init__(self, server="localhost", queue="mi_cola", user="Usuario1", passw="Contrasenia1"):
        self.servidor = server
        self.cola = queue
        self.credencial = pika.PlainCredentials(username=user, password=passw) # Configura las credenciales de RabbitMQ
        
    def enviar_json(self, archivo):
        connection = pika.BlockingConnection(pika.ConnectionParameters(self.servidor, credentials=self.credencial))

        channel = connection.channel()

        # Declaración de una cola
        channel.queue_declare(queue=self.cola)

        # Lee el contenido del archivo JSON
        with open(archivo, 'r') as file:
            contenido_json = file.read()

        # Enviar el contenido del archivo JSON como mensaje
        channel.basic_publish(exchange='',
                              routing_key=self.cola,
                              body=contenido_json)

        print(f"JSON de '{archivo}' enviado")

        # Cerrar la conexión
        connection.close()

#Prueba del Publisher (exitosa)
#pub = Publisher()
#pub.enviar_json("registros.json")