from flask import Flask
from settings import settings
from gevent import monkey
from gevent.pywsgi import WSGIServer
from werkzeug.routing import BaseConverter
from util.find_handlers import load_all_handlers
# monkey.patch_all()


class RegexConverter(BaseConverter):
    def __init__(self, map, *args):
        self.map = map
        self.regex = args[0]


app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter

load_all_handlers(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{name}:{pwd}@{host}/{db}'.format(
    name=settings.DB_ACCOUNT,
    pwd=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    db=settings.DB_NAME
)

print(str(app.url_map).replace("Map([", " ").strip("])"))

if __name__ == '__main__':
    #http_server = WSGIServer(('', 5000), app)
    #http_server.serve_forever()
    app.run(thread=True)

