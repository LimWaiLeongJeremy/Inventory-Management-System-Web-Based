from decorators.auth_decorator import require_login
from flask import Blueprint, render_template
 

# ========== Create blueprint ==========
route_bp = Blueprint(
    "route", 
    __name__, 
    template_folder="../../frontend"
)


# Routing frontend
@route_bp.route('/')
@route_bp.route('/login')
def login():
    return render_template("login.html")

# Routing dashboard
@route_bp.route('/dashboard')
@require_login
def dashboard():
    return render_template("dashboard.html")