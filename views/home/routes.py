from flask import Blueprint, render_template

home = Blueprint("home", __name__)

@home.route("/")
def r_home():
    import markdown as md
    file = open("README.md")
    md = md.markdown(file.read(), extensions=["fenced_code", "codehilite"])
    file.close()
    return render_template("docs.html", md=md)