import web

class auth:
    def __init__(self):
        pass

    def login(self, user, passwd):
        web.debug(user)
        web.debug(passwd)
        if(user != None and passwd != None and user == passwd):
            web.debug("AUTHED")
            web.config.session.user = True
            return True
        return False

