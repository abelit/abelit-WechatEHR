from werkzeug.wrappers import Request

class BlockMiddle(object):
    def __init__(self, wsgi_app):
        # super().__init__()
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        # return super().__call__(*args, **kwargs)
        # do something ...
        request = Request(environ)

        # 获取真实地址
        if request.headers.getlist("X-Forwarded-For"):
            ip = request.headers.getlist("X-Forwarded-For")[0]
        else:
            ip = request.remote_addr

        # print(ip)
        # print(request.headers.get('Authorization'))
        print("before middleware ......")
        # print(request.path)
        # print(request.args)
        # print(environ)

        app = self.wsgi_app(environ, start_response)

        print("after middleware ......")

        return app
