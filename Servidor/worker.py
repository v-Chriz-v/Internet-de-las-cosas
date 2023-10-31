import pika
import json
from func_sqlite import *

# Función que se ejecuta cuando se recibe un mensaje
def callback(ch, method, properties, body):
    mensaje_json = json.loads(body) #Leyendo json recibido
    
    print(f"Mensaje recibido...")
    
    #Guardar datos a la bd
    print(f"Guardando datos en la base de datos...")
    almacenar_datos(mensaje_json, "instance/basededatos.db")

# Configura las credenciales de RabbitMQ
credencial = pika.PlainCredentials(username='Usuario1', password='Contrasenia1')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credencial))

channel = connection.channel()

# Declaración de una cola
channel.queue_declare(queue='datos_sensores')

# Definir la función de callback para manejar los mensajes
channel.basic_consume(queue='datos_sensores', on_message_callback=callback, auto_ack=True)

print("EJECUTANDO WORKER")
print('Esperando mensajes. Para salir, presiona CTRL+C')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    print("Cerrando worker")