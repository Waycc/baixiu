import json
from settings import settings
from util import url, MethodView
from model.admin.baixiu_dev import User
from flask import (
    Blueprint, redirect, request, render_template, make_response)

login = Blueprint('login', __name__, url_prefix="")


@url('/adminLogin.html', login)
class AdminLogin(MethodView):
    """
    处理后台登录
    """
    LOGIN_URL = "/adminLogin.html"

    def get(self):
        if self.get_session():
            return redirect(settings.ADMIN_INDEX)
        return render_template('admin/login.html')

    def post(self):
        email = request.values.get("email")
        pwd = request.values.get("password")
        next_path = request.values.get("next")
        user = User.query.filter_by(email=email, password=pwd).first()
        result = {"status": False, "msg": "", "next": ""}
        if user:
            result["status"] = True
            result["next"] = next_path or settings.ADMIN_INDEX
            rep = make_response(json.dumps(result))
            self.set_session(rep, {"user":user.to_dict()})
            return rep

        return self.json(result)

@url("/adminLogout", login)
class AdminLogout(MethodView):
    def get(self):
        self.logout()
        return redirect(settings.LOGIN_URL)