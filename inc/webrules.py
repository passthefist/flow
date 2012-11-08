import web

class must:

    @staticmethod
    def be_logged_in(fn):
        web.debug("LOG IN TEST")
        def func(*args):
            web.debug("LOGG IN")
            web.debug(web.ctx)
            if web.config.session.get('user', False):
                return fn(*args)
            else:
                raise web.seeother('/static/login.html')
        return func

