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

from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_restful import Api, Resource


def create_home(app):
    from wechatehr.app.home.views import homebp

    # register blueprint
    app.register_blueprint(homebp)

def create_auth(app):
    from wechatehr.app.auth.views import authbp
    app.register_blueprint(authbp, url_prefix="/api/v1/auth")

def create_ehr(app):
    from wechatehr.app.ehr.views import ehrbp
    from wechatehr.app.ehr.views import ehrapi
    from wechatehr.app.ehr.views import EHRJob,EHRJobList

    ehrapi.add_resource(EHRJob, '/job', endpoint="jobs")
    ehrapi.add_resource(EHRJobList, '/job/<string:id>', endpoint="job")
    app.register_blueprint(ehrbp, url_prefix="/api/v1/ehr")

def create_app():
    from wechatehr.db import db
    from wechatehr.config import config

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

    # middle
    @_app.before_first_request
    def middle_first_request():
        print("first acccessing " + request.path + " from " + request.remote_addr)

    @_app.before_request
    def middle_start_request():
        print("start acccessing " + request.path + " from " + request.remote_addr)

    @_app.after_request
    def middle_end_request(response):
        print("finnish  acccessing " + request.path + " from " + request.path )
        return response
    
    create_home(_app)  if 'home' in _app.config['APPS'] else None
    create_ehr(_app) if 'ehr' in _app.config['APPS'] else None
    create_auth(_app) if 'auth' in _app.config['APPS'] else None

    return _app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)