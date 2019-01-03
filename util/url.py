def url(pattern, blue):
    """
    用于@url("/", blue), 方便设置路由映射
    """
    def wrap(cls, *args, **kwargs):
        blue.add_url_rule(pattern, view_func=cls.as_view(cls.__name__.lower()))
    return wrap