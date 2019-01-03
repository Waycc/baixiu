from util.url import url
from flask import views
from flask import Blueprint
from flask import request, render_template

account = Blueprint('account', __name__, url_prefix="/account")


@url('/', account)
class Login(views.MethodView):
    def get(self):
        return "111111111"

