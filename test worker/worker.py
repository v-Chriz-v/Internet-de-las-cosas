import pika
import json

# Función que se ejecuta cuando se recibe un mensaje
def callback(ch, method, properties, body):
    mensaje_json = json.loads(body)
    print(f"Mensaje recibido: {mensaje_json}")
    # Realiza aquí cualquier operación que desees con el JSON

# Conexión a RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declaración de una cola
channel.queue_declare(queue='mi_cola')

# Definir la función de callback para manejar los mensajes
channel.basic_consume(queue='mi_cola', on_message_callback=callback, auto_ack=True)

print('Esperando mensajes. Para salir, presiona CTRL+C')
channel.start_consuming()
