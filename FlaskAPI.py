from flask import Flask, jsonify
import json
from Consumer import Consumer

app = Flask(__name__)
consumer = Consumer()

# Ruta para obtener registros desde el archivo JSON
#El archivo lo debe de cosneguir desde Rabbit
@app.route('/registros', methods=['GET'])
def obtener_registros():
    try:
        with open('data/registros.json', 'r') as json_file:
            registros = json.load(json_file)
        return jsonify({"registros": registros})
    except FileNotFoundError:
        return jsonify({"error": "El archivo de registros no se encuentra"})

#El API debe guardar los datos obtenidos en la base de datos
@app.route('/consumir', methods=['GET'])
def consumir_cola():
    
    

#El API debe hacer una query de los datos hacia el usuario


if __name__ == '__main__':
    app.run(debug=True)
