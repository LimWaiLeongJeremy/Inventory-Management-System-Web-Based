import traceback

from repo.prod_repo import get_product_by_location_repo, get_location_by_product_repo

def get_product_by_location_svc(location):
    try:
        status, result = get_product_by_location_repo(location)
        # Check if data exists
        if not result:
            return False, "Invalid location"
        
        return status, result
    # Raise exception if failed
    except Exception:
        traceback.print_exc()
        raise     
    

def get_location_by_product_svc(product_name):
    try:
        status, result = get_location_by_product_repo(product_name)
        # Check if data exists
        if not result:
            return False, "Invalid product"
        
        return status, result
    # Raise exception if failed
    except Exception:
        traceback.print_exc()
        raise   