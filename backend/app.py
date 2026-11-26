import os

from flask import Flask
from flask_jwt_extended import JWTManager

from datetime import timedelta
from controllers.loc_controller import  location_bp
from controllers.prod_controller import product_bp
from controllers.user_controller import user_bp
from controllers.route_controller import route_bp

# Frontend files live in ../frontend; resolve it so it works no matter where the script is run from
FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontend"))

# Only frontend/assets is served as plain files (e.g. /assets/css/login.css).
# HTML pages are served by route_controller, so login checks like @require_login
# cannot be skipped by opening /dashboard.html directly.
app = Flask(
    __name__,
    static_folder=os.path.join(FRONTEND_DIR, "assets"),
    static_url_path="/assets"
)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=30)

# Initialize JWT with the main app
jwt = JWTManager()
jwt.init_app(app)

# Register controllers
app.register_blueprint(location_bp)
app.register_blueprint(product_bp)
app.register_blueprint(user_bp)
app.register_blueprint(route_bp)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
