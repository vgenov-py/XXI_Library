from flask import Blueprint,  request, render_template
from db import QMO
import json
import msgspec

web = Blueprint("web", __name__)

@web.route("/")
def t_web():
    qmo_1 = QMO("geo", {})
    fields = json.dumps(qmo_1.all_fields)
    if request.args:
        args = dict(request.args)
        args["is_from_web"] = True
        dataset = args.pop("dataset")
        qmo_1 = QMO(dataset,args)
        data = qmo_1.json()
        if data["success"]:
            data["data"] = tuple(data["data"])
            data = msgspec.json.encode(data)
            data = json.loads(data)
            data["data"] = data["data"][:10]
        return render_template("web/index.html", fields = fields, data=json.dumps(data))
    return render_template("web/index.html", fields = fields)    