from flask import Flask
from flask_cors import CORS

from controllers.controller import product_bp

app = Flask(__name__)
CORS(app)

# ========== Register controllers ==========
app.register_blueprint(product_bp)


if __name__ == '__main__':
    app.run(debug=True, port=5000)


