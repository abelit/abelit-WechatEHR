# -*- encoding: utf-8 -*-
'''
@File    :   users.py
@Time    :   2020/12/16 15:24:15
@Author  :   Abelit 
@Version :   1.0
@Contact :   ychenid@live.com
@Copyright :   (C)Copyright 2020, dataforum.org
@Licence :   BSD-3-Clause
@Desc    :   None
'''


from wechatehr.db import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import uuid


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    alias = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100), unique=True,
                     nullable=False, doc="user account")
    surname = db.Column(db.String(100), nullable=False, doc="real username")
    email = db.Column(db.String(200), unique=True,
                      nullable=False, doc="user email, can login as email")
    phone = db.Column(db.String(11), unique=True,
                      nullable=True, doc="phone")
    password = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.Integer, nullable=False, doc="1:male,0:female")
    role = db.Column(db.String(100),
                     nullable=True, default='normal',doc="role")
    wechat = db.Column(db.String(200),
                     nullable=True, default='',doc="wechat")
    status = db.Column(db.Integer, default=1, doc="0 permmited, 1: allow")
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_timestamp = db.Column(
        db.DateTime, nullable=False, onupdate=datetime.now, default=datetime.now)