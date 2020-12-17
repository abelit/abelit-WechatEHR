from werkzeug.wrappers import Request

class RoleMiddle(object):
    def __init__(self, wsgi_app):
        # super().__init__()
        self.wsgi_app = wsgi_app
    
    def __call__(self, environ, start_response):
        # return super().__call__(*args, **kwargs)
        # do something ...
        request = Request(environ)
        print("middleware ......")
        print(request.path)
        print(request.args)
        return self.wsgi_app(environ, start_response)