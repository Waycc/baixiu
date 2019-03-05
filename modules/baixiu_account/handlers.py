from util.url import url
from util.my_method_view import AuthMethodView, MethodView
from flask import Blueprint
from flask import request, render_template
from model.admin.baixiu_dev import User, db

account = Blueprint('account', __name__, url_prefix="/account")

@url('/userInfo', account)
class userInfo(AuthMethodView):
    def get(self):
        user = self.get_current_user()
        return self.success(data=user)

@url('/user', account)
class _User(MethodView):
    def get(self):
        user_id = request.values.get("userId", 1)
        user = User.query.get(user_id)
        if not user:
            return self.fail(msg='没有找到用户%s'%user_id)
        return self.success(data=user.to_dict())


@url('/user/add', account)
class UserAdd(MethodView):
    def post(self):
       user_data = request.json
       if not user_data:
           return self.fail(msg='参数为空')
       user_obj = User(**user_data)
       db.session.add(user_obj)
       db.session.commit()
       return self.success()


