from flask import Flask, jsonify, request, abort
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import sqlite3
from datetime import datetime
from flask_cors import CORS

#Conexion de la API a la base de datos
#La base de datos MySQL
#Se usa pymysql
app = Flask(__name__)
db_name = "basededatos.db" 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
CORS(app)

class Datos(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Tiempo = db.Column(db.DateTime)
    Vibracion = db.Column(db.Float)
    Latitud = db.Column(db.String)
    Longitud = db.Column(db.String)
    Captura = db.Column(db.LargeBinary)
    Anormal = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'Tiempo': self.Tiempo,  
            'Vibracion': self.Vibracion,
            'Latitud': self.Latitud,
            'Longitud': self.Longitud,
            'Captura': self.Captura,
            'Anormal': self.Anormal
        }
    
@app.route('/api/datos', methods=['GET'])
def get_datos():
    datos = Datos.query.order_by(Datos.Tiempo).all()

    # Convertir los datos a un formato JSON
    datos_json = []
    for i in range(len(datos) - 1):
        dato_actual = datos[i]
        dato_siguiente = datos[i + 1]

        tiempo_actual = dato_actual.Tiempo
        tiempo_siguiente = dato_siguiente.Tiempo

        diferencia_tiempo = (tiempo_siguiente - tiempo_actual).total_seconds()

        if diferencia_tiempo <= 10:
            datos_json.append(dato_actual.to_dict())

    return jsonify(datos_json)


@app.route('/api/datos/fecha', methods=['GET'])
def obtenerDatosFecha():
    fecha = request.args.get('fecha', default = '', type = str)
    conn = sqlite3.connect('./dataServer/basededatos.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Datos WHERE DATE(Tiempo) = DATE(?)", (fecha,))
    datos = cursor.fetchall()

    if len(datos) == 0:
        abort(404, description="No se encontraron datos para la fecha especificada")

    # Convertir los datos a un formato JSON
    datos_json = []
    for dato in datos:
        dato_dict = {
            'id': dato[0],
            'Tiempo': dato[1],
            'Vibracion': dato[2],
            'Latitud': dato[3],
            'Longitud': dato[4],
            'Captura': dato[5],
            'Anormal': dato[6]
        }
        datos_json.append(dato_dict)

    return jsonify(datos_json)

#El API debe hacer una query de los datos hacia el usuario


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

