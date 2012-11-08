class tbl(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def get(self, key, default=None):
        if key not in self.__dict__:
            return default
        return self.__dict__[key]
