from flask import Blueprint, render_template, request
errors = Blueprint("errors", __name__)
import datetime as dt
from views.api.routes import write_error

@errors.app_errorhandler(404)
def error_404(error):
    return render_template("errors/404.html", message=f"/{request.url.split('/')[-1]} no es una URL disponible"), 404

@errors.app_errorhandler(403)
def error_403(error):
    return render_template("errors/404.html"), 403

@errors.app_errorhandler(500)
def error_500(error):
    return render_template("errors/404.html"), 500
