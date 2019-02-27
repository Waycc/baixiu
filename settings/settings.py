import os

BASE_DIR = os.getcwd()
print(BASE_DIR)

DB_HOST = 'localhost'
DB_PORT = 3306
DB_NAME = 'baixiu'
DB_ACCOUNT = 'root'
DB_PASSWORD = '123456'

MODULES_PATH = 'modules'  # 视图函数路径

LOGIN_URL = '/adminLogin.html'  # 登录地址
LOGIN_COOKIE_NAME = 'auth'  # seesion存放的key
ADMIN_INDEX = '/admin/index.html'

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_MAX_CONNECTIONS = 100

SESSION_KEY = 'baixiu_session'

SESSION_BACKEND = 'redis'

ALLOW_CROS_HOST = '*'
ALLOW_CROS_METHODS = 'OPTIONS,GET,POST'
ALLOW_CROS_HEADERS = 'content-type'
