from util import url, MethodView
from bson import ObjectId
from flask import (
    Blueprint, redirect, request, render_template, make_response)

login = Blueprint('login', __name__, url_prefix="")


@url('/adminLogin.html', login)
class AdminLogin(MethodView):
    LOGIN_URL = "/adminLogin.html"

    def get(self):
        return render_template('admin/login.html')

    def post(self):
        email = request.form.get("email")
        pwd = request.form.get("password")
        if email and pwd:
            rep = make_response(redirect("/admin/index.html"))
            self.set_session(rep, {"user":[email, pwd]})
            return rep

        return redirect("/adminLogin.html")
