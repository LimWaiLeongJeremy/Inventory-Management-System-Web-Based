from repo.prod_repo import get_product_by_location_repo, get_location_by_product_repo

def get_product_by_location_svc(location):
    result = get_product_by_location_repo(location)
    return result

def get_location_by_product_svc(product_name):
    result = get_location_by_product_repo(product_name)
    print("here")
    return result

