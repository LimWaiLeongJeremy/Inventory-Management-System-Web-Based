import traceback

from repo.loc_repo import get_all_locations_repo, get_zone_by_loc_repo, get_loc_exist_repo

def get_locations_svc():
    try:
        status, result = get_all_locations_repo()
        # Check if data exists
        if not result:
            return False, "could not find location"
        
        return status, result
    # Raise exception if failed
    except Exception:
        traceback.print_exc()
        raise     


def get_loc_exist_svc(location_code):
    try:
        exists = get_loc_exist_repo(location_code)
        # Check if data exists
        if not exists:
            return exists
        
        return exists
    # Raise exception if failed
    except Exception:
        traceback.print_exc()
        raise     

def get_zone_by_loc_svc(location_code):
    try:
        status, result = get_zone_by_loc_repo(location_code)
        # Check if data exists
        if not result:
            return False, "could not find zones"
        
        return status, result
    # Raise exception if failed
    except Exception:
        traceback.print_exc()
        raise     

