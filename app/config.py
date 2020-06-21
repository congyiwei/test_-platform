# -*- coding: utf-8 -*-
# @Time    : 2020-06-18 22:33
# @Author  : CongYiWei
# @Email   : 1056285392@qq.com
# @File    : config.py
# @Software: PyCharm


class BaseConfig:
    PER_PAGE = 10
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/test_platform'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProdConfig(BaseConfig):
    pass


class TestConfig(BaseConfig):
    DEBUG = True


config = DevelopmentConfig()
