import traceback

from flask import (
    Blueprint, 
    jsonify,
    request
)
from flask_jwt_extended import jwt_required, get_jwt

from services.prod_svc import (
    get_product_by_location_zone_bin_svc, 
    get_location_by_product_svc,
    stock_transfer_svc
)

# ========== Create blueprint ==========
product_bp = Blueprint("product", __name__)



# product api
@product_bp.route('/api/product/<string:location_code>/<int:zone_id>/<int:bin_id>/', methods=['GET'])
@jwt_required()
def get_prod_by_loc_api(location_code, zone_id, bin_id):    
    # validate json value
    if not isinstance(location_code, str) or not location_code:
        return jsonify({
            "status": "error",
            "data": "location cannot be empty"
        }), 400

    if not isinstance(zone_id, int) or not zone_id:
        return jsonify({
            "status": "error",
            "data": "zone cannot be empty"
        }), 400
        
    if not isinstance(bin_id, int) or not bin_id:
        return jsonify({
            "status": "error",
            "data": "bin cannot be empty"
        }), 400

    try:
        success, products = get_product_by_location_zone_bin_svc(location_code, zone_id, bin_id)

        if not success:
                return jsonify({
                    "status": "error",
                    "data": products
                }),409
        return jsonify({
            'status': "success",
            'products': [prod.to_dict() for prod in products]
        }), 200

    except Exception:
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "data": "Internal server error"
        }), 500


# Stock transfer api
@product_bp.route('/api/product/transfer/', methods=['POST'])
# @jwt_required()
def stock_transfer_api():   
    # get data from body
    data = request.get_json()  

    # Validate if body has content
    if data is None:
        return jsonify({
            "status": "error",
            "data": "Invalid or missing JSON data"
        }), 400

    # retriving datas
    location_id = data.get('location_id', "")
    product_barcode = data.get('product_barcode', "")
    quantity = data.get('quantity', "")

    # validate json value
    if not isinstance(location_id, int) or not location_id:
        return jsonify({
            "status": "error",
            "data": "location cannot be empty"
        }), 400

    if not isinstance(product_barcode, str) or not product_barcode:
        return jsonify({
            "status": "error",
            "data": "product cannot be empty"
        }), 400

    if not isinstance(quantity, int) or not quantity:
        return jsonify({
            "status": "error",
            "data": "quantity cannot be empty"
        }), 400
        

    try:
        success, stock_level = stock_transfer_svc(location_id, product_barcode, quantity)

        if not success:
                return jsonify({
                    "status": "error",
                    "data": stock_level
                }),409
        return jsonify({
            'status': "success",
            'stock_level': [stk.to_dict() for stk in stock_level]
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
    if claims.get("role") == "user":
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