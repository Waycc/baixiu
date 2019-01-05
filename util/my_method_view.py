from flask import views, request, redirect
from bson import ObjectId
from util.session import session
from settings import settings


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
            return redirect(self.LOGIN_URL or settings.LOGIN_URL)
        return super(AuthMethodView, self).dispatch_request(*args, **kwargs)



