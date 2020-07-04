import hashlib

from flask import Flask, request, render_template, redirect, make_response, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1qaz@WSX@127.0.0.1:3306/flask_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    passwd = db.Column(db.String(100))

    def __repr__(self):
        return self.name


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        username = request.form.get("username")
        passwd = request.form.get("passwd")
        md5 = hashlib.md5()
        md5.update(passwd.encode("utf-8"))
        passwd = md5.hexdigest()
        print(username, passwd)
        user = User(name=username, passwd=passwd)
        db.session.add(user)
        db.session.commit()
        resp = make_response("注册成功！")
        return resp



if __name__ == "__main__":
    db.create_all()