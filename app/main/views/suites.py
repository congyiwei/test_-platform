# -*- coding: utf-8 -*-
# @Time    : 2020-06-30 22:17
# @Author  : CongYiWei
# @Email   : 1056285392@qq.com
# @File    : suites.py
# @Software: PyCharm
from app.main import main


@main.route("/suites")
def suites():
    return "suites"


@main.route("/create_suites")
def create_suites():
    return "create_suites"
