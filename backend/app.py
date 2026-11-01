from flask import Flask
from flask_cors import CORS

from controllers.loc_controller import  location_bp

app = Flask(__name__)
CORS(app)

# ========== Register controllers ==========
app.register_blueprint(location_bp)


if __name__ == '__main__':
    app.run(debug=True, port=5000)


