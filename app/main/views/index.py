# -*- coding: utf-8 -*-
# @Time    : 2020-06-18 23:18
# @Author  : CongYiWei
# @Email   : 1056285392@qq.com
# @File    : index.py
# @Software: PyCharm
from flask import render_template

from app.main import main


@main.route("/")
def index():
    projects = [
        {"project_name": "云", "project_number": "30", "modules_number": "2"},
        {"project_name": "雾", "project_number": "31", "modules_number": "3"},
        {"project_name": "风", "project_number": "32", "modules_number": "4"},
        {"project_name": "雨", "project_number": "33", "modules_number": "5"},
        {"project_name": "雷", "project_number": "34", "modules_number": "6"}
    ]
    return render_template("index.html", projects = projects)
