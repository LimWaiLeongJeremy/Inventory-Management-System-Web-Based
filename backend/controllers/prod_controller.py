import traceback

from flask import Blueprint, jsonify

from services.prod_svc import get_product_by_location_svc, get_location_by_product_svc

# ========== Create blueprint ==========
product_bp = Blueprint("product", __name__)



# product api
@product_bp.route('/api/locations/<string:location_name>/products', methods=['GET'])
def get_prod_by_loc_api(location_name):
    # Validate if body has content
    if data is None:
        return jsonify({
            "status": "error",
            "data": "Invalid or missing JSON data"
        }), 400
    
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
            'data': products
        }), 200

    except Exception:
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "data": "Internal server error"
        }), 500


@product_bp.route('/api/product/<string:product_name>/summary', methods=['GET'])
def get_loc_by_prod_api(product_name):
    # Validate if body has content
    if data is None:
        return jsonify({
            "status": "error",
            "data": "Invalid or missing JSON data"
        }), 400
    
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
            'data': products
        }), 200

    except Exception:
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "data": "Internal server error"
        }), 500