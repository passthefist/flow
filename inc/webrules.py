import web
from models.user import user

class must:

    @staticmethod
    def be_logged_in(fn):
        def func(*args):
            if web.config.session.get('user', False):
                return fn(*args)
            else:
                raise web.seeother('/static/login.html')
        return func

    @staticmethod
    def have_value(value, responder):
        def wrap(fn):
            def func(*args):
                user = web.config.session.user
                if user.vals.get(value, False):
                    return fn(*args)
                return responder(*args)
            return func
        return wrap
