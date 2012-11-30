import web
from inc.structs import *
from controllers import *
from db.session import Session as db_session

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

web.config.dbpath = 'sqlite:///db/flow.db'

if __name__ == "__main__":
    app = web.application(urls, globals())
    web.config.session = web.session.Session(app, web.session.DiskStore('sessions'))
    app.add_processor(db_session.load)

    app.run()
