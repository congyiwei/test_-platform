# -*- coding: utf-8 -*-
# @Time    : 2020-06-21 22:42
# @Author  : CongYiWei
# @Email   : 1056285392@qq.com
# @File    : projects.py
# @Software: PyCharm
from app.main import main


@main.route("/list_projects")
def list_projects():
    return "list_projects"


@main.route("/create_project", methods=['POST', 'GET'])
def create_project():
    return "create_project"
