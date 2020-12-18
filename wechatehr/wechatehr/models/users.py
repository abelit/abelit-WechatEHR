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


from sqlalchemy.orm import backref
from wechatehr.db import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import uuid



roles_apis = db.Table('roles_apis',
                      db.Column('roleid', db.Integer, db.ForeignKey(
                          'roles.id'), primary_key=True),
                      db.Column('apiid', db.Integer, db.ForeignKey(
                          'apis.id'), primary_key=True),
                      db.Column('created_timestamp', db.DateTime,
                                nullable=False, default=datetime.now),
                      db.Column('updated_timestamp', db.DateTime,
                                nullable=False,  onupdate=datetime.now, default=datetime.now)
                      )


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
    roleid = db.Column(db.Integer, db.ForeignKey('roles.id'),
                       nullable=False, doc="role",)
    wechat = db.Column(db.String(200),
                       nullable=True, default='', doc="wechat")
    status = db.Column(db.Integer, default=1, doc="0 permmited, 1: allow")
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_timestamp = db.Column(
        db.DateTime, nullable=False, onupdate=datetime.now, default=datetime.now)


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    alias = db.Column(db.String(100), nullable=True)
    name = db.Column(db.String(100), unique=True,
                     nullable=False, doc="role name")
    status = db.Column(db.Integer, nullable=False,
                       default=1, doc="0:disable,1:enable")
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_timestamp = db.Column(
        db.DateTime, nullable=False, onupdate=datetime.now, default=datetime.now)

    users = db.relationship('User', backref='roles', lazy=True)
    apis = db.relationship('Api', secondary=roles_apis, lazy='subquery',
                           backref=db.backref('roles', lazy=True))


class Api(db.Model):
    __tablename__ = "apis"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True,
                     nullable=False, doc="Api Endpoint name")
    path = db.Column(db.String(2000),
                     nullable=False, doc="Api Endpoint path")
    status = db.Column(db.Integer, nullable=False,
                       default=1, doc="0:disable,1:enable")
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_timestamp = db.Column(
        db.DateTime, nullable=False, onupdate=datetime.now, default=datetime.now)

