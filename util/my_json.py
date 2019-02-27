import json
import datetime
from model.admin.baixiu_dev import db
from flask_sqlalchemy import BaseQuery


class MyJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, BaseQuery):
            return list(map(lambda x: x.to_dict(), obj))
        elif isinstance(obj, db.Model):
            return obj.to_dict()
        elif isinstance(obj, (datetime.datetime,)):
            return obj.isoformat()
        else:
            return super(MyJSONEncoder, self).default(obj)


def dumps(*args, **kwargs):
    return json.dumps(cls=MyJSONEncoder, *args, **kwargs)


def loads(*args, **kwargs):
    return json.loads(*args, **kwargs)


def dump(*args, **kwargs):
    return json.dump(*args, **kwargs)


def load(*args, **kwargs):
    return json.load(*args, **kwargs)
