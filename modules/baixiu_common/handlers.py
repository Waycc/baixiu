import os
import time
from settings import settings
from util.url import url
from util.my_method_view import AuthMethodView
from flask import Blueprint
from flask import request, render_template

account = Blueprint('common', __name__, url_prefix="")

@url('/imageUpload', account)
class ImageUpload(AuthMethodView):
    def post(self):
        img = request.files.get("editormd-image-file")
        filename = "%s%s" % (int(time.time()), img.filename)
        img_path = os.path.join(settings.BASE_DIR, "static", "uploads", "users", filename)
        img.save(img_path)
        result = {
            "success": 1,
            "message": "上传成功",
            "url": "/static/uploads/users/%s" % filename
        }
        return self.json(result)

