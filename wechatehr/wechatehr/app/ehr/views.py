from flask import json, render_template, Blueprint, request, jsonify, current_app
from flask_restful import Api, Resource, abort,request

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

class EHRJob(Resource):
    def get(self):
        abort(401)
        return jsonify({
            "name": "ehrjob",
            "method": "get"
        })
        
    def post(self):
        return jsonify({
            "name": "ehrjob",
            "method": "post"
        })

    def put(self):
        return jsonify({
            "name": "job",
            "method": "put"
        })

    def delete(self):
        return jsonify({
            "name": "job",
            "method": "delete"
        })

    def patch(self):
        return jsonify({
            "name": "job",
            "method": "patch"
        })

class EHRJobList(Resource):
    def get(self,id):
        return jsonify({
            "name": "ehrjob",
            "method": "get",
            "params": id
        })
        
    def post(self,id):
        return jsonify({
            "name": "ehrjob",
            "method": "post",
            "params": id,
        })