import json
from util.get_redis import redis_client
from settings import settings


class Session(dict):

    def __getattr__(self, item):
        return self.get(item, None)

    def __setattr__(self, key, value):
        self[key] = value

    def __getitem__(self, item):
        return super(Session, self).__getitem__(item)

    def __setitem__(self, key, value):
        super(Session, self).__setitem__(key, value)

    def remove(self, name):
        self.pop(name, None)


class RedisSession(Session):
    session_key = settings.SESSION_KEY

    def __getitem__(self, item):

        session_value = redis_client.get(item)
        if session_value:
            session_value = json.loads(session_value.decode("utf-8"))
       
        return session_value

    def __setitem__(self, key, value):
        if not isinstance(value, dict):
            raise Exception("session value is not dict")
        value = json.dumps(value)
        redis_client.set(key, value)

    def get(self, name, default=None):
        return self[name] or default
        

    def remove(self, name):
        redis_client.delete(name)


if settings.SESSION_BACKEND == "redis":
    session = RedisSession()
else:
    session = Session()

