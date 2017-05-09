import webapp2
from jinja import JINJA_ENVIRONMENT
from thread import Thread

class Home(webapp2.RequestHandler):
    def get(self):
        template_values = {'threads':Thread.query().order(Thread.timestamp)}
        template = JINJA_ENVIRONMENT.get_template("templates/home.html")
        self.response.write(template.render(template_values));
