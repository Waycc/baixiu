from util.url import url
from flask import views
from flask import Blueprint
from flask import request, render_template, make_response
from flask import abort
from util.my_method_view import AuthMethodView
from .handlers import admin


#@url('/post/list', admin)
#class PostList(AuthMethodView):
#    def get(self, page_name):
#        page_path = "admin/dist/index.html"
#        return render_template(page_path)
