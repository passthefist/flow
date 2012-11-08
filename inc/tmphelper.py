class tbl(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, key, value):
        self.__dict__[key] = value
