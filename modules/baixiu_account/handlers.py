from util.url import url
from util import AuthMethodView
from flask import Blueprint
from flask import request, render_template

account = Blueprint('account', __name__, url_prefix="/account")

@url('/userInfo', account)
class userInfo(AuthMethodView):
    def get(self):
        user = self.get_current_user()
        return self.json(user)

