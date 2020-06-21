# -*- coding: utf-8 -*-
# @Time    : 2020-06-17 22:46
# @Author  : CongYiWei
# @Email   : 1056285392@qq.com
# @File    : __init__.py.py
# @Software: PyCharm
"""web服务器运行     初始化app核心对象
选用uwsgi
配置相关插件
"""
from flask import Flask
from flask_migrate import Migrate

from app.config import config
from app.main.models import db

app = Flask(__name__)
migrate = Migrate()
migrate.init_app(app, db)


# 其他初始化东西，数据库
# 初始化app
def create_app():
    # 配置文件
    app.config.from_object(config)
    # 初始化数据库
    db.init_app(app)
    # 自定义的错误处理机制
    # 模板过滤器注册
    # 注册蓝图
    from app.main import main
    app.register_blueprint(main)
    return app
