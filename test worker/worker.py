import pika
import json

# Función que se ejecuta cuando se recibe un mensaje
def callback(ch, method, properties, body):
    mensaje_json = json.loads(body)
    
    # Especifica el nombre del archivo en el que deseas guardar el JSON
    archivo_salida = "archivo_salida.json"
    
    with open(archivo_salida, 'w') as file:
        # Escribe el JSON en el archivo
        json.dump(mensaje_json, file, indent=4)
    
    print(f"Mensaje recibido y guardado en {archivo_salida}")

# Conexión a RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declaración de una cola
channel.queue_declare(queue='mi_cola')

# Definir la función de callback para manejar los mensajes
channel.basic_consume(queue='mi_cola', on_message_callback=callback, auto_ack=True)

print('Esperando mensajes. Para salir, presiona CTRL+C')
channel.start_consuming()
