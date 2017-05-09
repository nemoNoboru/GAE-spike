from thread import Thread
from jinja import JINJA_ENVIRONMENT
import webapp2

class ThreadCreator(webapp2.RequestHandler):
    def get(self):
        # serve the creation form
        template = JINJA_ENVIRONMENT.get_template("templates/create_thread.html")
        self.response.write(template.render());

    def post(self):
        # create new thread
        try:
            thread = Thread()
            thread.title = self.request.get('title')
            thread.body = self.request.get('body')
            thread.image = self.request.get('pic')
            thread.put()
            self.redirect('/')
        except:
            template = JINJA_ENVIRONMENT.get_template("templates/error_thread.html")
            self.response.write(template.render())
