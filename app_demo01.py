from flask import Flask, jsonify, render_template
import json


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

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


if __name__ == "__main__":
    app.run(debug=True)