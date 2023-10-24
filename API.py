from fastapi import FastAPI
import json


app = FastAPI()

# Ruta para obtener registros desde el archivo JSON
@app.get("/registros")
def obtener_registros():
    try:
        with open("data/registros.json", "r") as json_file:
            registros = json.load(json_file)
        return {"registros": registros}
    except FileNotFoundError:
        return {"error": "El archivo de registros no se encuentra"}

@app.get("/Registros")
def consumir_registros():
    