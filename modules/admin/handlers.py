# from util.url import url
# from flask import views
# from flask import Blueprint
# from flask import request, render_template
#
# admin = Blueprint('admin', __name__, url_prefix="/admin")
#
# @url('/<regex("[a-zA-Z0-9]+"):page_name>.html', admin)
# class ShowPage(views.MethodView):
#     def get(self, page_name):
#         page_path = "admin/%s.html"%page_name
#         return render_template(page_path)