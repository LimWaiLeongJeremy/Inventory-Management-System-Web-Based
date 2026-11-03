from repo.prod_repo import get_product_by_location, get_location_by_product

def get_all_product_by_location(location):
    result = get_product_by_location(location)
    return result

def get_all_location_by_product(product_name):
    result = get_location_by_product(product_name)
    print("here")
    return result

