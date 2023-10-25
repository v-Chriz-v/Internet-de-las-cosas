import pika
import json

# Conexión a RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declaración de una cola
channel.queue_declare(queue='mi_cola')

# JSON a enviar
json_data = {
    "nombre": "Ejemplo",
    "edad": 30,
    "ciudad": "Ejemploville"
}

# Convertir el JSON en una cadena JSON
mensaje_json = json.dumps(json_data)

# Enviar el mensaje a la cola
channel.basic_publish(exchange='',
                      routing_key='mi_cola',
                      body=mensaje_json)

print(f"JSON enviado: {mensaje_json}")

# Cerrar la conexión
connection.close()
