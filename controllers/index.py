import web
from inc.webrules import must

render = web.template.render('templates/')

class actions:

    def GET(self):
        web.debug("INDEX")
        conf = web.config.appconf
        return render.flow(github=conf.github)

