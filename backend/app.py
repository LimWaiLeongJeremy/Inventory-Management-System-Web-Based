import os
import psycopg

from urllib.parse import urlsplit, urlunsplit
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template
from flask_cors import CORS

load_dotenv() # must run before Config is imported

from config import Config
from extensions import db


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
CORS(app)

def _to_psycopg_url(url: str) -> str:
    """Convert SQLAlchemy URL (postgresql+psycopg://) to a plain libpq URL."""
    parts = urlsplit(url)
    # Strip the '+psycopg' / '+psycopg2' dialect suffix from the scheme
    scheme = parts.scheme.split("+", 1)[0]
    return urlunsplit((scheme, parts.netloc, parts.path, parts.query, parts.fragment))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api', methods=['GET'])
def hello_world():
    return "Hello World"


@app.route('/api/greet/<name>', methods=['GET'])
def greet_name(name):
    return f"Hello {name}"


@app.route("/api/db-check", methods=["GET"])
def db_check():
    database_url = os.environ.get("DATABASE_URL")
    if not database_url:
        app.logger.error("DATABASE_URL is not configured")
        return jsonify({
            "status": "error",
            "message": "Database configuration is missing",
        }), 503

    sslmode = os.environ.get("DB_SSLMODE", "prefer")

    try:
        with psycopg.connect(
            _to_psycopg_url(database_url),
            connect_timeout=5,
            sslmode=sslmode,
        ) as conn:
            conn.execute("SELECT 1")

        return jsonify({
            "status": "success",
            "message": "Database connection successful",
        }), 200

    except Exception:
        app.logger.exception("Database connection failed")
        return jsonify({
            "status": "error",
            "message": "Database connection failed",
        }), 503


if __name__ == '__main__':
    app.run(debug=True, port=5000)