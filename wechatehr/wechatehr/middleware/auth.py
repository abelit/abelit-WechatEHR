from functools import wraps
from flask_jwt_extended import get_jwt_identity

def role_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("permission required ...")
        print(get_jwt_identity())
        return fn(*args, **kwargs)

    return wrapper