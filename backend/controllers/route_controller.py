from flask import Blueprint, render_template
 

# ========== Create blueprint ==========
route_bp = Blueprint(
    "route", 
    __name__, 
    template_folder="../../frontend"
)


# Routing frontend
@route_bp.route('/')
def home():
    return render_template("login.html")

# Routing dashboard
@route_bp.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")