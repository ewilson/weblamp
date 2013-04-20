import web
import flash

urls = (
    '/weblamp', 'index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base='layout')

class index:
    def GET(self):
        switch = web.input()
        switch.light = 'on' if flash.read() else 'off'
        return render.weblamp(switch = switch)
    
    def POST(self):
        switch = web.input()
        flash.switch(switch.light == 'on')
        return render.weblamp(switch = switch)

if __name__ == '__main__':
    app.run()

