class TestFlaskExtend(object):
    # custom extend for flask
    def __init__(self, app=None):
        self.app = app
        if self.app is not None:
            self.init_app(app)

    # factory method to build app
    def init_app(self, app):
        print("testextend init app...")
        self.app = app