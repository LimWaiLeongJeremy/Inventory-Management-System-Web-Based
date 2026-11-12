from flask import Blueprint, render_template
 

# ========== Create blueprint ==========
route_bp = Blueprint("route", __name__)


# Routing frontend
@route_bp.route('/')
def home():
    return render_template("/login.html")

