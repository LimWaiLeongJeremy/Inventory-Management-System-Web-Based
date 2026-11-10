import os
import threading
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from controllers.loc_controller import  location_bp
from controllers.prod_controller import product_bp
from controllers.user_controller import user_bp

app = Flask(__name__)
CORS(app)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

# Initialize JWT with the main app
jwt = JWTManager()
jwt.init_app(app)

# Register controllers
app.register_blueprint(location_bp)
app.register_blueprint(product_bp)
app.register_blueprint(user_bp)


# Frontend server 
FRONTEND_HOST = "127.0.0.1"
FRONTEND_PORT = 5500 # change number if port is taken
FRONTEND_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontend")


# Serve files from the frontend folder, no matter where the script is run from
class FrontendHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=FRONTEND_DIR, **kwargs)


def start_frontend_server():
    # Fails with "address already in use" if the port is taken, instead of moving to another port
    server = ThreadingHTTPServer((FRONTEND_HOST, FRONTEND_PORT), FrontendHandler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    print(f" * Frontend running on http://{FRONTEND_HOST}:{FRONTEND_PORT}/login.html")


if __name__ == '__main__':
    # Debug mode runs this file twice (a watcher + the real app);
    # only start the frontend in the real app so port 5500 is not taken twice
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        start_frontend_server()

    app.run(debug=True, port=5000) #api port


