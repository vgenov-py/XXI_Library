from flask import Blueprint,  request, render_template, Response, g, send_file
from db import QMO
import time
import datetime as dt
import cProfile
import pstats
import msgspec
from fields import fields
from views.api.utils import write_error
from re import sub

api = Blueprint("api", __name__)

@api.route("/")
def r_home():
    '''
    Ésta ruta se encarga de convertir el md a formato HTML haciendo uso de la librería markdown
    El README contiene los siguientes puntos:
    1. Explicación de uso
    2. Tutorial
    3. Ejemplos de consulta
    '''
    import markdown as md
    file = open("README.md")
    md = md.markdown(file.read(), extensions=["fenced_code", "codehilite"])
    file.close()
    return render_template("docs.html", md=md)

@api.route("/<model>")
def r_query(model):
    '''
    Ésta es la ruta más compleja del blueprint api
    Hace uso de las siguientes librerías:
    msgspsec: msgspec, permite convertir colecciones de datos tanto ordenadas como asociativas en JSON.
    Hace uso de _structs_ para ofrecer los menores tiempos de respuesta registrado entre otras alternativas como: json, orjson, ujson
    Pensar en los structs como si fueran objetos en Python, por cada modelo existente en la DB (per, ent, geo...), crea un modelo que permite hacer la conversión velozmente

    El resto del código es un conjunto de pasos secuenciales lógicos:
    1. Recibir los argumentos del cliente
    2. Consultar la db con esos argumentos
    3. Entrejar un fichero csv o json si el cliente lo ha solicitado o sino
    4. Entregar un JSON limitado siempre a 1000 resultados
    '''
    model = sub("\.csv|\.json", "", model)
    args = {}
    for k,arg in request.args.items():
        args[k] = sub("\.csv|\.json", "", arg)
    file_extension = request.url.rsplit(".", 1)[-1]
    # with cProfile.Profile() as pr: # http://localhost:3000/api/per?t_375=masculino&limit=1000000 # código comentado  que sirve para evaluar el rendimiento de la respuesta
    qmo_1 = QMO(model, args)
    if model not in qmo_1.datasets + ["queries"]:
        return render_template("errors/404.html", message=f"{model} no es un conjunto de datos existente")
    
    data = qmo_1.json() # Éste método está explicado en db.py
    if file_extension in ("csv", "json"):
        if not data["success"]:
            return {"success": False, "message": f"No se ha podido generar el {file_extension}", "error": data["message"]}
        if file_extension == "csv":
            try:
                file_name = qmo_1.export_csv()
                return send_file(f"{file_name}.zip", mimetype="text/csv")
            except Exception as e:
                write_error(40, f"{e}", "Couldn't export csv")
                return {"success":False, "message": "No se ha podido generar el csv"}
        elif file_extension == "json":
            try:
                file_name = qmo_1.export_json()
                return send_file(f"{file_name}.zip", mimetype="text/csv")
            except Exception as e:
                write_error(41, f"{e}", "Couldn't export json")
                return {"success":False, "message": "No se ha podido generar el json"}

    # data = qmo_1.json()
    print(f"{request.url}".center(100,"-"))
    if data["success"]:
        data["time"] = time.perf_counter()
        data["data"] = tuple(data["data"])
        data["time"] = time.perf_counter() - data["time"]
        if model == "queries":
            data["length"] = len(data["data"]) 
        now = dt.datetime.now()
        try:
            if model != "queries":
                g._database = None
                qmo_1.enter(data["query"], None, now, model, data["time"],request.args.get("is_from_web"), False,True)
        except Exception as e:
            write_error(2,f"{e}", "Couldn't save query")
        data.pop("query")
    try:    
        data = msgspec.json.encode(data) # convertir cada diccionario en el iterable a un struct para luego generar el JSON
    except Exception as e:
        write_error(3, f"{e}", "Error ocurred while encoding data using msgspec")
    res = Response(response=data, mimetype="application/json", status=200) # application/gzip
    # stats = pstats.Stats(pr) # código comentado  que sirve para evaluar el rendimiento de la respuesta
    # stats.sort_stats(pstats.SortKey.TIME) # código comentado  que sirve para evaluar el rendimiento de la respuesta
    # stats.print_stats(8) # código comentado  que sirve para evaluar el rendimiento de la respuesta
    return res

@api.route("/fields/<model>")
def r_fields(model):
    '''
    Ésta ruta tiene como objetivo indicar los campos o esquema del modelo solicitado.
    '''
    res = {}
    test_QMO = QMO(model)
    view = request.args.get("view")
    if view:
        if view == "human":
            res["fields"] = test_QMO.human_fields
        elif view == "marc":
            res["fields"] = test_QMO.marc_fields
        return res
    res["fields"] = test_QMO.available_fields
    return res

@api.route("/schema")
def t_schema():
    dataset = request.args.get("dataset")
    if dataset:
        if fields.get(dataset):
            return render_template("schema.html", fields=fields[dataset])
    return render_template("schema.html")
        
@api.route("/stats")
def t_stats():
    '''
    Gráficas de uso generadas con js utilizado la librería chart.js
    '''
    return render_template("stats.html")