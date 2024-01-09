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
    import markdown as md
    file = open("README.md")
    md = md.markdown(file.read(), extensions=["fenced_code", "codehilite"])
    file.close()
    return render_template("docs.html", md=md)

@api.route("/<model>")
def r_query(model):
    model = sub("\.csv|\.json", "", model)
    args = {}
    for k,arg in request.args.items():
        args[k] = sub("\.csv|\.json", "", arg)
    file_extension = request.url.rsplit(".", 1)[-1]
    # with cProfile.Profile() as pr: # http://localhost:3000/api/per?t_375=masculino&limit=1000000
    qmo_1 = QMO(model, args)
    if model not in qmo_1.datasets + ["queries"]:
        return render_template("errors/404.html", message=f"{model} no es un conjunto de datos existente")
    
    data = qmo_1.json()
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
        data = msgspec.json.encode(data)
    except Exception as e:
        write_error(3, f"{e}", "Error ocurred while encoding data using msgspec")
    res = Response(response=data, mimetype="application/json", status=200) # application/gzip
    # stats = pstats.Stats(pr)
    # stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats(8)
    return res

@api.route("/fields/<model>")
def r_fields(model):
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
    return render_template("stats.html")