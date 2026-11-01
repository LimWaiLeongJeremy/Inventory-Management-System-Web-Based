from flask import Blueprint, jsonify

from services.prod_svc import get_all_product_by_location, get_all_product_summary


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
def getProdSum(product_name):
    products = get_all_product_summary(product_name)

    return jsonify({
        'status': "success",
        'product name': product_name,
        'data': products
    }), 200

# # @product_bp.route('/api/products/<string:product_id>/locations', methods=['GET'])
# # def getProLoc(product_id):
# #     product_info = None
# #     locations = []
# #     total_quantity = 0

# #     for loc in location: 
# #         for product in loc['product']:
# #             if product['product_id'] == product_id:
# #                 if product_info is None:
# #                     product_info = {
# #                         'product_id': product['product_id'],
# #                         'sku': product['sku'],
# #                         'name': product['name']
# #                     }
# #                 locations.append({
# #                     'location_id': loc['location_id'],
# #                     'location_name': loc['location_name'],
# #                     'quntity': product['unit']
# #                 })
# #                 total_quantity += product['unit']

# #     if product_info is None: 
# #         return jsonify({
# #             'status': 'error',
# #             'message': 'Product not found'
# #         }), 404
    
# #     return jsonify({
# #         'status': 'success',
# #         'data': {
# #             **product_info,
# #             'total_quantity': total_quantity,
# #             'location': locations
# #         }
# #     }), 200
