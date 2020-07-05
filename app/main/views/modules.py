# -*- coding: utf-8 -*-
# @Time    : 2020-06-21 22:43
# @Author  : CongYiWei
# @Email   : 1056285392@qq.com
# @File    : modules.py
# @Software: PyCharm
from app.main import main


@main.route("/list_modules")
def list_modules():
    return "list_modules"


@main.route("/create_module")
def create_module():
    return "create_module"


@main.route("/get_module/<int:m_id>", methods=["GET", "POST"])
def get_module(m_id=None):
    return f'get_module{m_id}'


@main.route("/edit_module/<int:m_id>", methods=["GET", "POST"])
def edit_module(m_id=None):
    return f'edit_module{m_id}'


@main.route("/delete_module", methods=["POST"])
def delete_module():
    return "delete_module"
