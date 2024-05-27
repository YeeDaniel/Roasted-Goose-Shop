from flask import request, render_template, redirect, url_for, flash, Blueprint, session, jsonify
from services import UserService
import re

user = Blueprint('user', __name__, template_folder='templates')

@user.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    if not re.match(r'^[\w\.-]+@gmail\.com$', email):
        return jsonify({'error': '電子郵件必須符合格式: XXX@gmail.com'}), 400

    if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d^#@$!%*?&]{8,}$', password):
        return jsonify({'error': '密碼必須超過8個字元且包含英⽂⼤⼩寫和特殊字元'}), 400

    result = UserService.register(username, email, password)
    if result == "username_exists":
        return jsonify({'error': '此名稱已被使用'}), 400

    # Assuming UserService.register returns None or some value for a successful registration
    if result:
        return jsonify({'success': '註冊成功'}), 200
    else:
        return jsonify({'error': 'E-mail 已註冊，請使用登入'}), 400
    
@user.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    login_user = UserService.login(email, password)
    if login_user is None:
        return jsonify({'error': '名字或密碼錯誤'}), 400

    if login_user:
        session["logged_in"] = True
        return jsonify({'success': '登入成功'}), 200
    else:
        return jsonify({'error': '登入失敗'}), 400


@user.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("登出成功", "logout")
    return redirect(url_for("default.index"))