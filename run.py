from flask import Flask
from routes.main import main_bp
from routes.second import second_bp
from routes.third import third_bp

ourapp = Flask(__name__)

# Register blueprints
ourapp.register_blueprint(main_bp)
ourapp.register_blueprint(second_bp)
ourapp.register_blueprint(third_bp)

if __name__ == "__main__":
    ourapp.run(debug=True)
#    ourapp.run(host="127.0.0.1", port=8395)