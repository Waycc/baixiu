from util.url import url
from flask import views
from flask import request, render_template, make_response
from flask import abort
from util.my_method_view import AuthMethodView
from flask import Blueprint

admin = Blueprint('admin', __name__, url_prefix="/admin")

#@url('/<regex(".*"):page_name>.html', admin)
#class ShowPage(AuthMethodView):
#    # 当请求页面不存在时，应当返回404
#    ARROW_PAGE = {
#        "categories": True, "comments": True, "index": True, "login": False,
#        "nav-menus": True, "password-reset": True, "post-add": True, "posts": True,
#        "profile": True, "settings": True
#    }
#    def get(self, page_name):
#        if not self.ARROW_PAGE.get(page_name):
#            abort(404)
#        page_path = "admin/%s.html"%page_name
#        return render_template(page_path)

@url('/', admin)
class ShowPage(AuthMethodView):
    def get(self):
        page_path = "admin/dist/index.html"
        return render_template(page_path)
