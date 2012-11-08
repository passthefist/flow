import web
from inc.webrules import must

render = web.template.render('templates/')

class actions:
    @must.be_logged_in
    def GET(self):
            return "main"
