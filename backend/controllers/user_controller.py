from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt
from services.user_svc import user_auth_svc, user_create_svc
 

# ========== Create blueprint ==========
user_bp = Blueprint("auth", __name__)


# User API
@jwt_required
@user_bp.route('/api/user/create', methods=['POST'])
def user_create_api():
    # Check for access 
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({
            "status": "error",
            "data": "Forbidden"
        }), 403
    # get data from body
    data = request.get_json()  

    # Validate if body has content
    if data is None:
        return jsonify({
            "status": "error",
            "data": "Invalid or missing JSON data"
        }), 400
        
    # retriving datas
    username = data.get('username', "")
    password = data.get('password', "")
    fullname = data.get('fullname', "")
    role = data.get('role', "")

    # validate json value
    if not isinstance(username, str) or not username:
        return jsonify({
            "status": "error",
            "data": "Username cannot be empty"
        }), 400
    

    if not isinstance(password, str) or not password:
        return jsonify({
            "status": "error",
            "data": "Password cannot be empty"
        }), 400

    if len(password) < 8:
        return jsonify({
            "status": "error",
            "data": "Password must be at least 8 characters"
        }), 400

    # data sanitization
    username = username.strip().lower()
    role = role.strip().lower()

    # Try to create user 
    try:
        success, result = user_create_svc(username, fullname, password, role)
        if not success:
            return jsonify({
                "status": "error",
                "data": result
            }),409
            
        return jsonify({
            "status": "success",
            "data": result
        }), 200   

    except Exception:
        import traceback
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "data": "Internal server error"
        }), 500



@user_bp.route('/api/user/login', methods=['POST'])
def user_login_api():

# TODO
# look into modulize of data sanitization
    # get data from body
    data = request.get_json()  

    # Validate if body has content
    if data is None:
        return jsonify({
            "status": "error",
            "data": "Invalid or missing JSON data"
        }), 400

    # retriving datas
    username = data.get('username', "")
    password = data.get('password', "")

    # validate json value
    if not isinstance(username, str) or not username:
        return jsonify({
            "status": "error",
            "data": "Username cannot be empty"
        }), 400
    

    if not isinstance(password, str) or not password:
        return jsonify({
            "status": "error",
            "data": "Password cannot be empty"
        }), 400

    if len(password) < 8:
        return jsonify({
            "status": "error",
            "data": "Password must be at least 8 characters"
        }), 400

    # data sanitization
    username = username.strip().lower()

 # Try to create user 
    try:
        success, result = user_auth_svc(username, password)
        if not success:
            return jsonify({
                "status": "error",
                "data": result
            }),409
            
        return jsonify({
            "status": "success",
            "token": result
        }), 200   

# TODO 
# print all trace back like this
    except Exception:
        import traceback
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "data": "Internal server error"
        }), 500

