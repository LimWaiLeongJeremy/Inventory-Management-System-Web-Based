from repo.prod_repo import get_product_by_location, get_product_summary

def get_all_product_by_location(location):
    result = get_product_by_location(location)
    return result

def get_all_product_summary(product_name):
    result = get_product_summary(product_name)
    print("here")
    return result

