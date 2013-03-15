import web

urls = (
    '/weblamp', 'index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base='layout')

class index:
    def GET(self):
        switch = web.input(light='off')
        print switch.light
        return render.weblamp(switch = switch)
    
    def POST(self):
        switch = web.input(light='off')
        print switch.light
        return render.weblamp(switch = switch)

if __name__ == '__main__':
    app.run()

