import web
from inc.webrules import must

render = web.template.render('templates/issues/')

class actions:
    @must.be_logged_in
    def GET(self, item):
        web.debug(item)
        return render.__getattr__(item)()
