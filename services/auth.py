import web
from models.user import User

class auth:
    def __init__(self):
        pass

    def login(self, user, passwd):
        if(user != None and passwd != None and user == passwd):
            web.config.session.uid = user
            return True
        return False

    def loggedInUser(self):
        web.ctx.user = self.getUser(web.config.session.uid)
        return web.ctx.user

    def isAuthed(self):
        return web.config.session.get('uid', None) != None

    def getUser(self, user):
        mock = {
            'a' : User(),
            'b' : User(),
        }
        return mock.get(user, None)

