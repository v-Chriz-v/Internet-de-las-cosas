import pika

class Consumer:
    def __init__(self) -> None:
        pass
    
    def establecer_conexion(self):
        # Configurar la conexión con RabbitMQ
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='datos_sensores')  