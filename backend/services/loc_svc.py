import traceback

from repo.loc_repo import get_locations_repo

def get_locations_svc():
    try:
        status, result = get_locations_repo()
        # Check if data exists
        if not result:
            return False, "could not find location"
        
        return status, result
    # Raise exception if failed
    except Exception:
        traceback.print_exc()
        raise     

