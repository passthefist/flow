import web
from inc.structs import *
from controllers import *

print dir(index)

urls = (
    '/' , index.actions,
    '/pages/issues/(.+).html' , issues.actions,
    '/pages/main.html' , main.actions,
    '/login' , login.actions,
)

render = web.template.render('templates/')

web.config.appconf = tbl(
    github = tbl(
        url = 'http://github.com/',
        user = 'rdgoetz',
        passwd = 'password'
    )
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    web.config.session = web.session.Session(app, web.session.DiskStore('sessions'))

    app.run()
