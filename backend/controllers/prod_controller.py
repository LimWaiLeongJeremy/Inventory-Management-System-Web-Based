from flask import Blueprint, jsonify

from services.prod_svc import get_product_by_location_svc, get_location_by_product_svc

# ========== Create blueprint ==========
product_bp = Blueprint("product", __name__)



# product api
@product_bp.route('/api/locations/<string:location_name>/products', methods=['GET'])
def get_prod_by_loc_api(location_name):

    products = get_product_by_location_svc(location_name)

    return jsonify({
        'status': "success",
        'location': location_name,
        'data': products
    }), 200


@product_bp.route('/api/product/<string:product_name>/summary', methods=['GET'])
def get_loc_by_prod_api(product_name):
    products = get_location_by_product_svc(product_name)

    return jsonify({
        'status': "success",
        'product name': product_name,
        'data': products
    }), 200