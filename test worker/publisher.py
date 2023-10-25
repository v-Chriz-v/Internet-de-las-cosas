import pika
import json

# Configura las credenciales de RabbitMQ
credencial = pika.PlainCredentials(username='Usuario1', password='Contrasenia1')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credencial))

channel = connection.channel()

# Declaración de una cola
channel.queue_declare(queue='mi_cola')

# Nombre del archivo JSON que deseas enviar
nombre_archivo_json = "registros.json"

# Lee el contenido del archivo JSON
with open(nombre_archivo_json, 'r') as file:
    contenido_json = file.read()

# Enviar el contenido del archivo JSON como mensaje
channel.basic_publish(exchange='',
                      routing_key='mi_cola',
                      body=contenido_json)

print(f"JSON de '{nombre_archivo_json}' enviado")

# Cerrar la conexión
connection.close()
