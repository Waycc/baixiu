from util.url import url
from flask import views
from flask import Blueprint
from flask import request, render_template

admin = Blueprint('admin', __name__, url_prefix="/admin")

@url('/<regex("[\w\W]+"):page_name>.html', admin)
class ShowPage(views.MethodView):
    def get(self, page_name):
        page_path = "admin/%s.html"%page_name
        print(page_path)
        return render_template(page_path)