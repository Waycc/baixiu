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

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass


session = Session()
