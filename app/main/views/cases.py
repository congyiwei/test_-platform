# -*- coding: utf-8 -*-
# @Time    : 2020-06-21 22:43
# @Author  : CongYiWei
# @Email   : 1056285392@qq.com
# @File    : cases.py
# @Software: PyCharm
from app.main import main


@main.route("/list_cases")
def list_cases():
    return "list_cases"


@main.route("/create_case")
def create_case():
    return "create_case"
