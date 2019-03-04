import cgi
from datetime import datetime
from util.url import url
from modules.admin import admin
from flask import request, render_template, make_response
from util.my_method_view import AuthMethodView, MethodView
from model.admin.baixiu_dev import db, Category


@url('/category/list', admin)
class CategoryList(MethodView):

    def get(self):
        categories = Category.query
        count = categories.count()
        return self.success(data=categories, count=count)



@url('/category/add', admin)
class CategoryAdd(MethodView):

    def post(self):
        category_data = request.json
        if not category_data:
            return self.fail(msg='参数为空')       
        category_obj = Category(**category_data)
        db.session.add(category_obj)
        db.session.commit()
        return self.success()




