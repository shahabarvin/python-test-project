from flask import Blueprint, render_template

second_bp = Blueprint('second', __name__)

@second_bp.route("/second")
def secondroute():
    titleman = "Our second page"
    message = "This is the end of world ♥"
    return render_template("second_template.html", title=titleman, message=message)
