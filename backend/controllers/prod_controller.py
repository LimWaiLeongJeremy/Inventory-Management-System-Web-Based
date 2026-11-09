import traceback

from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt

from services.prod_svc import get_product_by_location_svc, get_location_by_product_svc

# ========== Create blueprint ==========
product_bp = Blueprint("product", __name__)



# product api
@product_bp.route('/api/locations/<string:location_name>/products', methods=['GET'])
@jwt_required()
def get_prod_by_loc_api(location_name):    
    # validate json value
    if not isinstance(location_name, str) or not location_name:
        return jsonify({
            "status": "error",
            "data": "location cannot be empty"
        }), 400

    try:
        success, products = get_product_by_location_svc(location_name)

        if not success:
                return jsonify({
                    "status": "error",
                    "data": result
                }),409
        return jsonify({
            'status': "success",
            'location': location_name,
            'products': [prod.to_dict() for prod in products]
        }), 200

    except Exception:
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "data": "Internal server error"
        }), 500


@product_bp.route('/api/product/<string:product_name>/summary', methods=['GET'])
@jwt_required()
def get_loc_by_prod_api(product_name):
    # Check for access 
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({
            "status": "error",
            "data": "Forbidden"
        }), 403

    # validate json value
    if not isinstance(product_name, str) or not product_name:
        return jsonify({
            "status": "error",
            "data": "product cannot be empty"
        }), 400

    try:
        success, products = get_location_by_product_svc(product_name)

        if not success:
                return jsonify({
                    "status": "error",
                    "data": result
                }),409
        return jsonify({
            'status': "success",
            'product name': product_name,
            'products': [prod.to_dict() for prod in products]
        }), 200

    except Exception:
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "data": "Internal server error"
        }), 500