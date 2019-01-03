from util.url import url
from flask import views
from flask import Blueprint
from flask import request, render_template

login = Blueprint('login', __name__, url_prefix="/login")


@url('/', login)
class Login(views.MethodView):
    def get(self):
        return render_template('baixiu_login/login.html')

