from flask import Flask
from settings import settings
from gevent import monkey
from gevent.pywsgi import WSGIServer
from flask import render_template
from werkzeug.routing import BaseConverter
from util.find_handlers import load_all_handlers
from model.admin.baixiu_dev import db
import os
# monkey.patch_all()


class _Flask(Flask):
    def run(self, *args, **kwargs):
        #load_all_handlers(self)

        #print(str(self.url_map).replace("Map([", " ").strip("])"))
        super(_Flask, self).run(*args, **kwargs)

class RegexConverter(BaseConverter):
    def __init__(self, map, *args):
        self.map = map
        self.regex = args[0]


app = _Flask(__name__)
app.url_map.converters['regex'] = RegexConverter
app.jinja_env.auto_reload = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{name}:{pwd}@{host}:{port}/{db}'.format(
    name=settings.DB_ACCOUNT,
    pwd=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    db=settings.DB_NAME
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

load_all_handlers(app)

print(str(app.url_map).replace("Map([", " ").strip("])"))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error_page/404.html'), 404





if __name__ == '__main__':
    #http_server = WSGIServer(('', 5000), app)
    #http_server.serve_forever()
    #app.run(host='0.0.0.0', port=8000, debug=True)
    app.run(host='127.0.0.1', port=8080, debug=True)

