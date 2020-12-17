from werkzeug.wrappers import Request
from flask_jwt_extended import get_jwt_identity

class RoleMiddle(object):
    def __init__(self, wsgi_app):
        # super().__init__()
        self.wsgi_app = wsgi_app
    
    def __call__(self, environ, start_response):
        # return super().__call__(*args, **kwargs)
        # do something ...
        # username = get_jwt_identity()
        request = Request(environ)
        # print(request.headers.get('Authorization'))
        print("middleware ......")
        # print(request.path)
        # print(request.args)
        # print(username)

        # print(environ)
        
        return self.wsgi_app(environ, start_response)