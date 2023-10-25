from flask import Flask, jsonify
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    db_name = "datashm" 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/' + db_name
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    return app

app = create_app()


# Ruta para obtener registros desde el archivo JSON
#El archivo lo debe de cosneguir desde Rabbit
@app.route('/registros', methods=['GET'])
def obtener_registros():
    try:
        with open('dataESP/registros.json', 'r') as json_file:
            registros = json.load(json_file)
        return jsonify({"registros": registros})
    except FileNotFoundError:
        return jsonify({"error": "El archivo de registros no se encuentra"})

@app.route('/test', methods=['GET'])
def testdb():
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return '<h1>It works.</h1>'
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

#El API debe hacer una query de los datos hacia el usuario


if __name__ == '__main__':
    app.run(debug=True)
