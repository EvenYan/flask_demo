import json

from flask import Flask, jsonify, render_template, request, redirect, url_for, make_response
from werkzeug.routing import BaseConverter


app = Flask(__name__)


@app.route("/home")
def index():
    username = request.cookies.get('user')
    return render_template("index.html", username=username)



@app.route("/")
def home():
    kw = request.args.get('wd')
    print(kw)
    return "欢迎来到我的首页"


@app.route("/getinfo")
def get_info():
    info = {		
        "name": "Tom",
        "age": 18
    }
    return jsonify(info)


@app.route("/get_data")
def get_data():
    demo_data = {"水果名称": ["苹果", "梨子", "香蕉", "橙子"], "水果销量": [14, 67, 23, 130]}
    return jsonify(demo_data)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        username = request.form.get("username")
        passwd = request.form.get("passwd")
        print(username, passwd)
        resp = make_response(redirect(url_for('index')))
        resp.set_cookie("user", username, max_age=60)
        return resp


@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    elif request.method == "POST":
        file = request.files.get("pic")
        if file:
            file.save("./pic.png")
            return "上传成功"
        else:
            return "文件上传失败"
        

@app.route("/post/<post_id>")
def get_post(post_id):
    return "这是第%s篇文章" % post_id


class PhoneNumConverter(BaseConverter):
    def __init__(self, url_map, regex):
        super().__init__(url_map)
        self.regex = regex

    def to_python(self, value):
        return value[:3] + "****" + value[-4:]

    def to_url(self, value):
        return value[:3] + "****" + value[-4:]


app.url_map.converters['re'] = PhoneNumConverter


@app.route('/call/<re(r"1\d{2}\*{4}\d{4}"):phone_number>')
def call_sb(phone_number):
    return "正在拨通%s的电话" % phone_number


@app.route("/call_my_brother")
def call():
    return redirect(url_for("call_sb", phone_number="13312345678"))


if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)


