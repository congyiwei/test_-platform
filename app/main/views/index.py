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
    return render_template("index.html")
