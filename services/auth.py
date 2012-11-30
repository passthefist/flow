import web
from models.user import User

class auth:
    def __init__(self):
        pass

    def login(self, user, passwd):
        if(user != None and passwd != None and user == passwd):
            web.config.session.uname = user
            web.config.session.uid = User.idFor(user)
            return True
        return False

    def loggedInUser(self):
        web.ctx.user = User.first(id = web.config.session.uid)
        return web.ctx.user

    def isAuthed(self):
        return web.config.session.get('uid', None) != None

