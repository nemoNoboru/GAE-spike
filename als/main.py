import webapp2
from app.thread_creator import ThreadCreator
from app.thread_detail import ThreadDetail
from app.home import Home

app = webapp2.WSGIApplication(
    [('/thread/new', ThreadCreator ),
     ('/', Home),
     ('/thread/detail', ThreadDetail)],debug=True
)
