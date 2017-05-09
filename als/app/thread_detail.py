from thread import Thread
from thread import Reply
import datetime
from jinja import JINJA_ENVIRONMENT
import webapp2

class ThreadDetail(webapp2.RequestHandler):
    def get(self):
        # serve a form to create replies, the thread and all the replies
        thread = Thread.get_by_id(int(self.request.get('key')))
        replies = Reply.query(Reply.thread == thread.key).order(Reply.timestamp)

        to_template = {'thread':thread, 'replies':replies}

        template = JINJA_ENVIRONMENT.get_template("templates/show_thread.html")
        self.response.write(template.render(to_template));

    def post(self):
        # create a reply
    #    try:
            thread = Thread.get_by_id(int(self.request.get('thread')))
            thread.timestamp = datetime.datetime.now()
            thread.put()
            reply = Reply()
            reply.title = self.request.get('title')
            reply.body = self.request.get('body')
            if(self.request.get('pic')):
                reply.image = self.request.get('pic')
            reply.thread = thread.key
            reply.put()
            self.redirect('/')
    #    except:
    #        template = JINJA_ENVIRONMENT.get_template("templates/error_thread.html")
    #        self.response.write(template.render())
