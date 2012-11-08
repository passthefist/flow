import web
from models.user import User
import services.auth as authService

auth = authService.auth()

class must:

    @staticmethod
    def be_logged_in(fn):
        def func(*args):
            if auth.isAuthed():
                return fn(*args)
            else:
                raise web.seeother('/static/login.html')
        return func

    @staticmethod
    def have_value(value, responder):
        def wrap(fn):
            def func(*args):
                user = auth.loggedInUser()

                if user.vals.get(value, False):
                    return fn(*args)
                return responder(*args)
            return func
        return wrap
