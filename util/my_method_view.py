import datetime
from flask import views, request, redirect
from bson import ObjectId
from util.session import session
from settings import settings
from flask import make_response
from util import my_json as json


class MethodView(views.MethodView):
    """
    不需要登录验证
    """

    def login(self, key, value):
        """
        用户登录, 仅仅是将登录信息写进session
        具体验证流程不在这里进行
        """
        session[key] = value

    def logout(self):
        """
        用户注销, 仅仅是从session去除用户信息
        """
        login_cookie = request.cookies.get(settings.LOGIN_COOKIE_NAME)
        if not login_cookie:
            return

        session.remove(login_cookie)

    def fail(self, status=False, error_code="", msg="", data="", _json=True, **kwargs):
        result = {
            "status": status,
            "error_code": error_code,
            'message': msg,
            'data': data
        }
        result.update(kwargs)
        if _json:
            return self.json(result)
        return result 

    def success(self, status=True, error_code="", msg="", data="", _json=True, **kwargs):
        result = {
            'status': status,
            'error_code': error_code,
            'message': msg,
            'data': data
        }
        result.update(kwargs)
        if _json:
            return self.json(result)
        return result 

    def get_current_user(self):
        current_session = self.get_session()
        user = current_session["user"]
        return user

    @staticmethod
    def get_session():
        key = request.cookies.get(settings.LOGIN_COOKIE_NAME)
        if not key:
            return None
        return session.get(key)

    @staticmethod
    def set_session(response, value, exp=None):
        """
        设置session, 同时将session的key设置在cookie
        """
        key = str(ObjectId())
        response.set_cookie(settings.LOGIN_COOKIE_NAME, key)
        session[key] = value

    @staticmethod
    def json(value, content_type="application/json;charset=UTF-8"):
        rep = make_response(json.dumps(value))
        rep.headers['Content-Type'] = content_type
        rep.headers['Access-Control-Allow-Origin'] = "*"
        return rep

    def handle_options(self):
        res = make_response()
        res.headers['Access-Control-Allow-Origin'] = settings.ALLOW_CROS_HOST
        res.headers['Access-Control-Allow-Headers'] = settings.ALLOW_CROS_HEADERS
        res.headers['Access-Control-Allow-Methods'] = settings.ALLOW_CROS_METHODS
        return res

    def options(self):
        pass

    def dispatch_request(self, *args, **kwargs):
        print("普通请求", request, "time: %s"%datetime.datetime.now())
        if request.method == 'OPTIONS':
            print("opyion!!!")
            return self.handle_options()
        return super(MethodView, self).dispatch_request(*args, **kwargs)

class AuthMethodView(MethodView):
    """
    增加登录验证逻辑
    """

    LOGIN_URL = None  # 默认从配置文件读取

    def check_login(self):
        auth_session = self.get_session()
        if not auth_session:
            return False
        return True

    def dispatch_request(self, *args, **kwargs):
        """
        重写这个方法，加入登录验证
        """
        is_login = self.check_login()
        if not is_login:
            print('没有登录的接口', request, "time: %s"%datetime.datetime.now())
            next_path = request.path
            login_url = self.LOGIN_URL or settings.LOGIN_URL
            return redirect(login_url + "?next=%s" % next_path)
        return super(AuthMethodView, self).dispatch_request(*args, **kwargs)



