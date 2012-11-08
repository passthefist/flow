import web
from inc.webrules import must

render = web.template.render('templates/')

class actions:
    @staticmethod
    def tutorial(self):
        return 'tutorial'

    @must.be_logged_in
    @must.have_value('tutorial', actions.tutorial)
    def GET(self):
            return "main"
