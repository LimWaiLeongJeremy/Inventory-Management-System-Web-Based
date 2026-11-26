from decorators.auth_decorator import require_login, require_role
from flask import Blueprint, redirect, render_template, session, url_for


# ========== Create blueprint ==========
route_bp = Blueprint(
    "route",
    __name__,
    template_folder="../../frontend"
)


# every template gets username and role (used by the sidebar in base.html)
@route_bp.app_context_processor
def add_user_to_templates():
    return {
        "username": session.get("username", ""),
        "role": session.get("role", "")
    }


# dont keep pages in the browser cache, so back after logging out can't show them
@route_bp.after_request
def no_store(response):
    response.headers["Cache-Control"] = "no-store"
    return response


# Routing frontend
@route_bp.route('/')
@route_bp.route('/login')
def login():
    return render_template("login.html")


# Overview: each role has its own design
@route_bp.route('/dashboard')
@require_login
def dashboard():
    role = session.get("role")

    if role == "admin":
        # admin has no overview, user management is their home page
        return redirect(url_for("route.users"))
    if role == "supervisor":
        return render_template("dashboard_supervisor.html")
    if role == "user":
        return render_template("dashboard_worker.html")

    # unknown role, log them out
    session.clear()
    return redirect(url_for("route.login"))


@route_bp.route('/stocktaking')
@require_login
@require_role("supervisor")
def stocktaking():
    return render_template("stocktaking.html")


@route_bp.route('/transfers')
@require_login
@require_role("supervisor", "user")
def transfers():
    return render_template("transfers.html")


@route_bp.route('/transactions')
@require_login
@require_role("supervisor", "user")
def transactions():
    return render_template("transactions.html")


# Bin details, opened from the zones & bins list on the overview
@route_bp.route('/bins/<bin_code>')
@require_login
@require_role("supervisor", "user")
def bin_details(bin_code):
    return render_template("bin.html", bin_code=bin_code)


@route_bp.route('/users')
@require_login
@require_role("admin")
def users():
    return render_template("users.html")
