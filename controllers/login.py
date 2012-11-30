import web
import services.auth as authService
import inc.responses as responses

render = web.template.render('templates/')

auth = authService.auth()

class actions:
    form = web.form.Form(
        web.form.Textbox("user"),
        web.form.Textbox("passwd"),
        web.form.Checkbox("forget")
    )

    def GET(self):
        return "LOGIN"

    @responses.json
    def POST(self):
        form = actions.form()

        if(form.validates()):
            user = form.d.user
            passwd = form.d.passwd

            if(auth.login(user,passwd)):
                print('logged in!')
                return { 'success': True }
        print('failed')
        return { 'success': False }
