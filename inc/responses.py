from functools import wraps
import json as JSON
import web

def json(func):
    @wraps(func)
    def wrapper(*args, **kw):
        value = func(*args, **kw)
        web.header("Content-Type", "application/json")
        return JSON.dumps(value)

    return wrapper
