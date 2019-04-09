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
        post_id = request.values.get('postId')
        if post_id:
            post_obj = Post.query.get(int(post_id))
            category_id = post_obj.category_id
            post_dict = post_obj.to_dict()
            category_obj = Category.query.get(category_id)
            post_dict['category_id'] = 0 if not category_obj else category_id
            return self.success(data=post_dict) 
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
        post_data.pop('postId', '')
        post_data['title'] = cgi.escape(post_data['title'])
        current_time = datetime.now()
        post_data['created'] = datetime.strftime(current_time, '%Y-%m-%d %H:%M:%S')
        post_data['updated'] = datetime.strftime(current_time, '%Y-%m-%d %H:%M:%S')
        post_obj = Post(**post_data)
        db.session.add(post_obj)
        db.session.commit()
        return self.success()


@url('/post/update', admin)
class PostUpdate(MethodView):
    def post(self):
        post_data = request.json
        post_id = post_data.pop('postId', '')
        print('postdata', post_data, post_id)
        if not post_data or not post_id:
            return self.fail(msg='参数或文章id为空')
        post_obj = Post.query.get(post_id)
        for k, v in post_data.items():
            setattr(post_obj, k, v)

        db.session.commit()
        return self.success()


@url('/post/delete', admin)
class PostDelete(MethodView):
    def post(self):
        post_id = request.form.get('postId')
        _post = Post.query.get(int(post_id))
        db.session.delete(_post)
        db.session.commit()
        return self.success()

@url('/post/batchDelete', admin)
class PostBatchDelete(MethodView):
    def post(self):
        post_ids = request.form.get('postIds', [])
        if not post_ids:
            return self.fail()
        _ids = list(map(lambda x: int(x), post_ids.split(',')))
        post_objs = Post.query.filter(Post.id.in_(_ids)).all()
        if post_objs:
            for p in post_objs:
                db.session.delete(p)
            db.session.commit()
        return self.success()
