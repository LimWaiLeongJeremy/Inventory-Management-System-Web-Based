import os

from flask import Flask, redirect
from flask_jwt_extended import JWTManager

from controllers.loc_controller import  location_bp
from controllers.prod_controller import product_bp
from controllers.user_controller import user_bp
from controllers.route_controller import route_bp

# Frontend files live in ../frontend; resolve it so it works no matter where the script is run from
FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontend"))

# Flask serves the whole frontend folder from the site root,
# e.g. /login.html and /assets/css/login.css
app = Flask(
    __name__, 
    static_folder=FRONTEND_DIR, 
    static_url_path=""
)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

# Initialize JWT with the main app
jwt = JWTManager()
jwt.init_app(app)

# Register controllers
app.register_blueprint(location_bp)
app.register_blueprint(product_bp)
app.register_blueprint(user_bp)
app.register_blueprint(route_bp)


@app.route("/")
def home():
    return redirect("/login.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
