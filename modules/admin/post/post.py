import cgi
from datetime import datetime
from util.url import url
from modules.admin import admin
from flask import request, render_template, make_response
from flask import abort
from util.my_method_view import AuthMethodView, MethodView
from model.admin.baixiu_dev import Post, db, Category, User


@url('/post/list', admin)
class PostList(MethodView):

    def get(self):
        page = int(request.values.get('page', 1))
        page_size = int(request.values.get('pageSize', 20))
        category_id = request.values.get('category_id', 'all')
        post_status = request.values.get('status', 'all')
        cond = {}
        if category_id != 'all':
            cond['category_id'] = category_id
        if post_status != 'all':
            cond['status'] = post_status

        posts = Post.query.filter_by(**cond)
        count = posts.count()
        posts = posts.offset((page-1)*page_size).limit(page_size)
        new_posts = []
        for each_post in posts:
            author_id = each_post.author_id
            category_id = each_post.category_id
            each_post = each_post.to_dict()
            each_post['category'] = Category.query.get(category_id)
            new_posts.append(each_post)

        return self.success(data=new_posts, count=count)

    def post(self):
        return self.get()


@url('/post/add', admin)
class PostAdd(MethodView):
    def post(self):
        post_data = request.json
        if not post_data:
            return self.fail(msg='参数为空')
        post_data['title'] = cgi.escape(post_data['title'])
        current_time = datetime.now()
        post_data['created'] = datetime.strftime(current_time, '%Y-%m-%d %H:%M:%S')
        post_data['updated'] = datetime.strftime(current_time, '%Y-%m-%d %H:%M:%S')
        post_obj = Post(**post_data)
        db.session.add(post_obj)
        db.session.commit()
        return self.success()


        

           
