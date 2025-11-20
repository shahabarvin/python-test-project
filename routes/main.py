from flask import Blueprint, Response

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def index():
    html = "<html><body><h1>Hello</h1><script>alert('havich farangi')</script></body></html>"
    return Response(html, mimetype="text/html")
