from flask import Blueprint, current_app, send_from_directory


# ========== Create blueprint ==========
route_bp = Blueprint("route", __name__)


# Routing frontend
@route_bp.route('/')
def home():
    return send_from_directory(current_app.static_folder, "login.html")