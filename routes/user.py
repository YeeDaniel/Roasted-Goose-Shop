from flask import request, render_template, redirect, url_for, flash, Blueprint
from services import UserService

user = Blueprint('user', __name__, template_folder='templates')

@user.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        result = UserService.register(username, email, password)
        if result:
            flash("註冊成功", "register")
            return redirect(url_for("user.login"))
        else:
            flash("E-mail 已註冊，請使用登入", "register")

    return render_template("index.html")

@user.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        login_user = UserService.login(email, password)
        if login_user:
            flash("登入成功", "login")
            return redirect(url_for("index.index"))
        else:
            flash("登入失敗", "login")

    return render_template("index.html")