from flask import request, jsonify, Blueprint, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity
)

from wechatehr.db import db
from wechatehr.models.users import User, Role, Api
from sqlalchemy import or_
import datetime

authbp = Blueprint('authbp', __name__)

@authbp.route('/ping')
def ping():
    return jsonify({
        "ping": "Pong!",
        "ip": request.remote_addr,
        "router": request.path,
        "module": __name__,
        "version": "v1"
    })

@authbp.route('/register', methods=['POST'])
def register():
    # 从前端Ajax请求中获取用户名
    username = request.json.get('username', None)
    surname = request.json.get('surname', None)
    alias = request.json.get('alias', None)
    email = request.json.get('email', None)
    phone = request.json.get('phone', None)
    gender = request.json.get('gender', None)
    role = request.json.get('role', None)
    wechat = request.json.get('wechat', None)
    password = request.json.get('password', None)
    # 用户注册默认状态为0即不允许登录, 1
    status = request.json.get('status', 1)

    status_code = None
    res = {"data": [], "msg": "", "code": None}

    user = User(surname=surname, username=username, alias=alias, email=email, phone=phone, gender=gender,
            role=role, wechat=wechat, password=generate_password_hash(password), status=status)
    try:
        db.session.add(user)
        db.session.commit()
        status_code = 200
        res["data"] = []
        res["msg"] = "add user sccuessfully"
        res["code"] = status_code
        
    except Exception:
        db.session.rollback()
        status_code = 500
        res["data"] = []
        res["msg"] = "add user failed"
        res["code"] = status_code

    return jsonify(res), status_code


@authbp.route('/login', methods=['POST'])
def login():
    # 从前端Ajax请求中获取用户名
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    status_code = None
    res = {"data": [], "msg": "", "code": None}
        # 获取用户信息
    filters = { 
        or_(
            User.username == username,
            User.phone == username,
            User.email == username
        )
    }

    try:
        user = User.query.filter(*filters).first()
        # 验证用户信息是否匹配
        if not user or not check_password_hash(user.password, password):
            status_code = 401
        else:
            # Use create_access_token() and create_refresh_token() to create our
            # access and refresh tokens
            access_expires = datetime.timedelta(seconds=current_app.config.get('JWT_ACCESS_TOKEN_EXPIRES'))
            refresh_expires = datetime.timedelta(seconds=current_app.config.get('JWT_REFRESH_ACCESS_TOKEN_EXPIRES'))
            status_code = 200
            res["data"] = [{
                'access_token': create_access_token(identity=user.username, expires_delta=access_expires),
                'refresh_token': create_refresh_token(identity=user.username, expires_delta=refresh_expires)
            }]
            res["msg"] = "get user successfully."
            res["code"] = status_code
    except:
        status_code = 500
        res["data"] = []
        res["msg"] = "get user failed."
        res["code"] = status_code

    return jsonify(res), status_code


# The jwt_refresh_token_required decorator insures a valid refresh
# token is present in the request before calling this endpoint. We
# can use the get_jwt_identity() function to get the identity of
# the refresh token, and use the create_access_token() function again
# to make a new access token for this identity.
@authbp.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    access_expires = datetime.timedelta(seconds=current_app.config.get('JWT_ACCESS_TOKEN_EXPIRES'))
    result = {
        'access_token': create_access_token(identity=current_user, expires_delta=access_expires)
    }
    return jsonify(result), 200


@authbp.route('/protected', methods=['GET'])
@jwt_required
def protected():
    username = get_jwt_identity()
    return jsonify(logged_in_as=username), 200

@authbp.route('/role/create', methods=['POST'])
def create_role():
    alias = request.json.get("alias", None)
    name =  request.json.get("name", None)
    status = request.json.get("status", 1)

    status_code = None
    res = {"data": [], "msg": "", "code": None}

    role = Role(alias=alias, name=name, status=status)
    try:
        db.session.add(role)
        db.session.commit()
        status_code = 200
        res["data"] = []
        res["msg"] = "add role sccuessfully"
        res["code"] = status_code
        
    except Exception:
        db.session.rollback()
        status_code = 500
        res["data"] = []
        res["msg"] = "add role failed"
        res["code"] = status_code

    return jsonify(res), status_code

@authbp.route('/api/create', methods=['POST'])
def create_api():
    name =  request.json.get("name", None)
    path = request.json.get("path", None)
    status = request.json.get("status", 1)

    status_code = None
    res = {"data": [], "msg": "", "code": None}

    api = Api(name=name, path=path, status=status)
    try:
        db.session.add(api)
        db.session.commit()
        status_code = 200
        res["data"] = []
        res["msg"] = "add api sccuessfully"
        res["code"] = status_code
        
    except Exception:
        db.session.rollback()
        status_code = 500
        res["data"] = []
        res["msg"] = "add api failed"
        res["code"] = status_code

    return jsonify(res), status_code
