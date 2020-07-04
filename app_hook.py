import json, hashlib

from flask import Flask, jsonify, render_template, request, redirect, url_for, make_response, g
from werkzeug.routing import BaseConverter


app = Flask(__name__)


@app.route("/")
def home():
    return "欢迎来到我的首页"


@app.route("/index")
def index():
    data_list = [1, 4, 7, "Java", ["Python", "PHP"]]
    people_dict = {"name": "Alice", "age": 20}
    return render_template('index1.html', data_list=data_list, people_dict=people_dict)

@app.before_first_request
def first_request():
    print("in first request")


@app.before_request
def before_request():
    black_ip_list = []
    ip = request.remote_addr
    if ip in black_ip_list:
        print("你的IP被限制了")
        raise Exception("你的IP被限制了")


if __name__ == "__main__":
    app.run(debug=True)


