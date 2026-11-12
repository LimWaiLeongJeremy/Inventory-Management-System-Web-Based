from flask import Blueprint, redirect
 

# ========== Create blueprint ==========
route_bp = Blueprint("route", __name__)


# Routing frontend
@route_bp.route('/')
def home():
    return redirect("/login.html")

