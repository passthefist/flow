import web
from inc.webrules import must

render = web.template.render('templates/')

def tutorial():

    return 'tutorial'

class actions:
    @staticmethod

    @must.be_logged_in
    @must.have_value('tutorial', tutorial)
    def GET(self):
            return "main"
