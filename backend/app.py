import os

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

# ========== Register controllers ==========
app.register_blueprint(location_bp)
app.register_blueprint(product_bp)
app.register_blueprint(user_bp)


if __name__ == '__main__':
    app.run(debug=True, port=5000)


