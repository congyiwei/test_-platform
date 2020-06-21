# -*- coding: utf-8 -*-
# @Time    : 2020-06-18 22:31
# @Author  : CongYiWei
# @Email   : 1056285392@qq.com
# @File    : __init__.py.py
# @Software: PyCharm
# 初始化蓝图
from flask import Blueprint
# url_prefix 给url增加前缀
# main = Blueprint("main", __name__, url_prefix="/main")
main = Blueprint("web", __name__)

# 路由
from .views import index

# 定义的时候 admin_backend = Blueprint("name", __name__)
# 路由导入定义的蓝图或者app
# 初始化app.register_blueprint(admin_backend)

