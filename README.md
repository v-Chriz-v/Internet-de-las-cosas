# Repositorio de Proyecto IoT (Ciudades)
## Integrantes
- Christian de Jesus Aguayo Anaya
- Alan Francisco Centeno Rosado
- Angel Daniel Lopez Alvarez
- Marco Antonio Alfaro Baruch

## Descripción del proyecto
El proyecto en este repositorio es el de albergar un sistema de salud estructural para los rieles de un tren. En este sistema, un dispositivo sensor captura los datos de vibración y ubicación junto a una captura de imagen cada determinado tiempo para enviarlo por una cola de mensajes donde un servidor recibe y guarda esa información en una base de datos que después, mediante una API, puede ser consultada por una aplicación.

De la misma manera, se detecta y se guarda la información sobre una lectura anormal de la vibración para su consulta posterior.

El sistema sensor, que simula una placa programable ESP32; el worker y la API están desarrolladas en el lenguaje de Python. El frontend o aplicación para consultar la información de la Base de Datos está hecha en HTML y JavaScript. La Base de Datos está hecha con la herramienta de SQLite.

Se utiliza RabbitMQ como sistema para manejar las colas de mensajes donde se envía y recibe la información.
## Elementos de la Infraestructura
Nuestra infraestructura consistirá en las siguientes partes:
- Sensores (vibración, GPS, cámara)
- Placa programable
- Base de datos.
- Servidor
- PC (Usuario)
![image](https://github.com/v-Chriz-v/Internet-de-las-cosas/assets/54341749/1bba9400-7ea3-4454-afc9-8446e4c895bb)
![image](https://github.com/v-Chriz-v/Internet-de-las-cosas/assets/147886154/e9627154-258d-43f4-84df-6e0ee29ab26a)

## Levantamiento del sistema
En este apartado se explica cómo el sistema debe ser levantado para su correcto funcionamiento.

### Servidor
#### Dependencias necesarias
Para poder ejecutar los elementos pertenecientes al Servidor en la infraestructura, es necesario tener las dependencias de Flask, CORS, SQLAlchemy y pika.

En caso de no contar con estas dependencias, iniciar el CMD y ejecutar los siguientes comandos:

`pip install flask`
`pip install flask-cors`
`pip install flask_sqlalchemy`
`pip install pika`

De la misma forma, se necesita tener RabbitMQ instalado en el sistema, así como tener una cuenta con el permiso de acceder al virtual host "/" con la siguiente información.

`Nombre de usuario: Usuario1`
`Contraseña: Contrasenia1`

#### Worker
El worker es el elemento que se encarga de escuchar la cola de mensajes y guardar la información en la base de datos. 

Para iniciar este servicio, basta con abrirlo desde el explorador de archivos o acceder a la carpeta Servidor en el CMD y ejecutar:
`python worker.py`

Al hacer esto, el servicio creará una cola, empezará a escuchar la información proveniente de esa cola y almacena la información gracias a funciones dentro del archivo "func_sqlite.py".

Para finalizar el worker, basta con presionar **Ctrl + C**.

#### FlaskAPI
La API implementada es la encargada de mandar información a través de la función GET que tiene incorporada, esto para hacer consultas a la base de datos hacia una aplicación.

El API cuenta con dos endpoints:
* `/api/datos` Manda la información de los ultimos 10 segundos
* `/api/datos/fecha` Manda todos los datos de un día en específico

Para iniciar este servicio, basta con abrirlo desde el explorador de archivos o acceder a la carpeta Servidor en el CMD y ejecutar:
`python FlaskAPI.py`

Al hacer esto, la API se levantará y la aplicación podrá realizar consultas a la base de datos a través de ella.

Para cerrar la API, basta con presionar **Ctrl + C**.

### Dispositivo sensor
#### Dependencias necesarias
Para poder ejecutar los elementos pertenecientes a la placa programable (ESP32) en la infraestructura, es necesario tener las dependencias de pika y CV2.

En caso de no contar con estas dependencias, iniciar el CMD y ejecutar los siguientes comandos:

`pip install opencv-python`
`pip install pika`

### Sensor v¿Vibracion
Genera valores de 0 a 1 que son considerados normales, con una probabilidad de un 20% de generar un valor anormal que es de 1.5 a 2.5.

### Sensor GPS
Genera valores aleatorios para latitud y longitud:
* Latitud: -90, 90
* Longitud: -180, 180

### Sensor cámara
Hace una captura y almacena la imagen en formato base64.
 
#### ESP
ESP es el encargado de capturar la información sobre la ubicación y vibración del tren, además de tomar una captura del momento. Después, la información es enviada por una cola de mensajes hacia el worker dentro del servidor. El ESP está configurado para mandar información durante 10 segundos representando "el recorrido" que hace el tren hasta una estación.

Para iniciar esta simulación de captura de información, basta con abrirlo desde el explorador de archivos o acceder a la carpeta ESP en el CMD y ejecutar:
`python ESP.py`

Al hacer esto, la API se levantará y la aplicación podrá realizar consultas a la base de datos a través de ella.

Para cerrar la API, basta con presionar **Ctrl + C**.

### Aplicación o interfaz
#### Frontend
La aplicación es una página en HTML que, utilizando JavaScript, realiza una consulta a la base de datos y obtiene los datos de ubicación, vibración y captura pertenecientes a esa fecha.

Para iniciar esta aplicación, basta con abrirla desde el explorador de archivos. Esto abrirá una ventana del navegador mostrando la aplicación. Para ver la información sobre las lecturas de un día, seleccione el día en el recuadro de abajo y presione Cargar Datos. Esto cargará la información solicitada.
