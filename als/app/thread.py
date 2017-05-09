from google.appengine.ext import ndb

class Thread(ndb.Model):
    title = ndb.StringProperty(required = True)
    body = ndb.StringProperty(required = True)
    timestamp = ndb.DateTimeProperty(auto_now = True)
    image = ndb.BlobProperty(required = True)

class Reply(ndb.Model):
    thread = ndb.KeyProperty(kind=Thread)
    title = ndb.StringProperty(required = False)
    body = ndb.StringProperty(required = True)
    timestamp = ndb.DateTimeProperty(auto_now = True)
    image = ndb.BlobProperty(required = False)
