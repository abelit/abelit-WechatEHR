from flask import json, render_template, Blueprint, request, jsonify, current_app
from flask_jwt_extended.utils import get_jwt_identity
from flask_restful import Api, Resource, abort,request

from flask_jwt_extended import jwt_required

ehrbp = Blueprint("ehrbp", __name__)

ehrapi = Api(ehrbp)

@ehrbp.route('/ping')
def ping():
    return jsonify({
        "ping": "Pong!",
        "ip": request.remote_addr,
        "router": request.path,
        "module": __name__,
        "version": "v1"
    })

class EHRJobList(Resource):
    @jwt_required
    def get(self):
        job_id = request.args.get('id')
        return {
            "name": self.__class__.__name__,
            "method": request.method,
            "job_id": job_id,
            "request_user": get_jwt_identity()
        }, 200
        
    def post(self):
        return {
            "name": self.__class__.__name__,
            "method": request.method,
        },201

    def put(self):
        return {
            "name": self.__class__.__name__,
            "method": request.method
        }, 201

    def delete(self):
        return jsonify({
            "name": self.__class__.__name__,
            "method": request.method,
        }), 204

    def patch(self):
        return {
            "name": self.__class__.__name__,
            "method": request.method,
        }, 201

class EHRJob(Resource):
    def get(self,id):
        job_id = request.args.get('id')
        return jsonify({
            "name": self.__class__.__name__,
            "method": request.method,
            "params": id,
            "jobid": job_id
        })
        
    def post(self,id):
        return jsonify({
            "name": self.__class__.__name__,
            "method": request.method,
            "params": id,
        })