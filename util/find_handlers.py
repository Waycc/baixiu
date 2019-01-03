import os
import importlib
from flask import Blueprint
from settings import settings

def load_all_handlers(app):
    """
    自动寻找所有视图函数，加载进app
    """
    moduels_path = os.path.join(os.getcwd(), settings.MODULES_PATH)
    def load_handlers(dir):
        for path in os.listdir(dir):
            current_path = os.path.join(dir, path)

            if os.path.isdir(current_path) and "__init__.py" in os.listdir(current_path):
                load_handlers(current_path)

            elif path.endswith(".py"):
                # 去掉前面的路径，得到导入模块的路径
                handler_path = current_path.replace(os.getcwd(), "").replace(os.sep, ".").strip(".").strip(".py")
                # 导入模块
                handler = importlib.import_module(handler_path)
                # 遍历模块中的所有对象，找到蓝图对象，注册到app中
                for v in handler.__dict__.values():
                    if isinstance(v, Blueprint):
                        app.register_blueprint(v)

    # 遍历当前modules， 加载所有视图函数
    for path in os.listdir(moduels_path):
        current_path = os.path.join(moduels_path, path)
        if os.path.isdir(current_path) and "__init__.py" in os.listdir(current_path):
            load_handlers(current_path)