# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2020/12/15 11:02:48
@Author  :   Abelit 
@Version :   1.0
@Contact :   ychenid@live.com
@Copyright :   (C)Copyright 2020, dataforum.org
@Licence :   BSD-3-Clause
@Desc    :   None
'''

from flask import Flask, json, request, jsonify,Response
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_jwt_extended.utils import get_jwt_identity
from flask_restful import Api, Resource


def create_home(app):
    from .app.home.views import homebp

    # register blueprint
    app.register_blueprint(homebp)

def create_auth(app):
    from .app.auth.views import authbp
    app.register_blueprint(authbp, url_prefix="/api/v1/auth")

def create_ehr(app):
    from .app.ehr.views import ehrbp
    from .app.ehr.views import ehrapi
    from .app.ehr.views import EHRJob,EHRJobList

    ehrapi.add_resource(EHRJobList, '/jobs', endpoint="jobs")
    ehrapi.add_resource(EHRJob, '/jobs/<string:id>', endpoint="job")
    app.register_blueprint(ehrbp, url_prefix="/api/v1/ehr")

def create_status_code(app): 
    @app.errorhandler(404)
    def not_found(err):
        return jsonify({"msg": str(err),"data": [],"code": 404}),404

    @app.errorhandler(401)
    def unauthorized(err):
        return jsonify({"msg": str(err),"data": [],"code": 401}),401

def create_app():
    from .db import db
    from .config import config

    from .middleware.blocklist import BlockMiddle
    from .extentions.testextend import TestFlaskExtend

    # create flask instance
    _app = Flask(__name__)

    # import config
    _app.config.from_object(config)
    config.init_app(_app)

    # add flask-sqlalchemy 
    db.init_app(_app)

    # set cross origin
    cors = CORS(_app, resources={r"/api/*": {"origins": "*"}})

    # create jwt instance
    jwt = JWTManager(_app)

    # register role verify middleware
    _app.wsgi_app = BlockMiddle(_app.wsgi_app)

    # custom extend for flask
    testext = TestFlaskExtend(_app)

    # middle
    @_app.before_first_request
    def middle_first_request():
        print("first acccessing " + request.path + " from " + request.remote_addr)

    @_app.before_request
    def middle_start_request():
        print("start acccessing " + request.path + " from " + request.remote_addr)
        # print(get_jwt_identity())

    @_app.after_request
    def middle_end_request(response):
        print("finnish  acccessing " + request.path + " from " + request.path )
        # print(get_jwt_identity())
        return response

    create_home(_app)  if 'home' in _app.config['APPS'] else None
    create_ehr(_app) if 'ehr' in _app.config['APPS'] else None
    create_auth(_app) if 'auth' in _app.config['APPS'] else None
    create_status_code(_app) if 'err' in _app.config['APPS'] else None

    return _app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)