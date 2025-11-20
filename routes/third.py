from flask import Blueprint, Response

third_bp = Blueprint('third', __name__)

@third_bp.route("/third")
def thirdroute():
    html = "<html><body><h1>our third page</h1></body></html>"
    return Response(html, mimetype="text/html")
