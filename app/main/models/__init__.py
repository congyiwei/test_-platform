# -*- coding: utf-8 -*-
# @Time    : 2020-06-21 21:56
# @Author  : CongYiWei
# @Email   : 1056285392@qq.com
# @File    : __init__.py
# @Software: PyCharm
import time

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    # 不生成表
    __abstract__ = True
    created_time = db.Column(db.Integer, default=int(time.time()))
    update_time = db.Column(db.Integer, default=int(time.time()), onupdate=int(time.time()))
    status = db.Column(db.SmallInteger, default=1)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, default='', unique=True)
