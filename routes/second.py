from flask import Blueprint, render_template

second_bp = Blueprint('second', __name__)

@second_bp.route("/second")
def secondroute():
    titleman = "Our second page"
    message = "این یک پیام نمونه است"
    return render_template("second_template.html", title=titleman, message=message)
