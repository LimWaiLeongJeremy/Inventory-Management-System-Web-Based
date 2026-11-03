from flask import Blueprint, jsonify

from services.prod_svc import get_all_product_by_location, get_all_location_by_product

# ========== Create blueprint ==========
product_bp = Blueprint("product", __name__)



# product api
@product_bp.route('/api/locations/<string:location_name>/products', methods=['GET'])
def getProdByLoc(location_name):

    products = get_all_product_by_location(location_name)

    return jsonify({
        'status': "success",
        'location': location_name,
        'data': products
    }), 200


@product_bp.route('/api/product/<string:product_name>/summary', methods=['GET'])
def getLocByProd(product_name):
    products = get_all_location_by_product(product_name)

    return jsonify({
        'status': "success",
        'product name': product_name,
        'data': products
    }), 200