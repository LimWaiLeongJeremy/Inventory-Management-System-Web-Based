from decorators.auth_decorator import require_login
from flask import Blueprint, make_response, render_template, session
 

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
    # signed-in username shown at the bottom of the sidebar
    response = make_response(render_template(
        "dashboard.html",
        username=session.get("username", ""),
        role=session.get("role", "")
    ))

    # dont keep a copy in the browser, so back after logging out can't show this page
    response.headers["Cache-Control"] = "no-store"
    return response