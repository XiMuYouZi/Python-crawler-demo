from flask import render_template
from . import main


@main.route('/', methods=['GET', ])
@main.route('/index', methods=['GET', ])
def get_depts():
    return '<div><h1>欢迎来到我的博客</h1></div>'
