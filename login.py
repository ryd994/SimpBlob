from google.appengine.api import users
from google.appengine.ext import webapp

providers = {
    'Google'   : 'https://www.google.com/accounts/o8/id',
    'Yahoo'    : 'yahoo.com',
    'MySpace'  : 'myspace.com',
    'AOL'      : 'aol.com',
    'MyOpenID' : 'myopenid.com'
    # add more here
}

class LoginHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Hello world! Sign in at: ')
        for name, uri in providers.items():
            self.response.out.write('[<a href="%s">%s</a>]' % (users.create_login_url(self.request.get('continue'), federated_identity=uri), name))

app = webapp.WSGIApplication([
    ('/_ah/login_required', LoginHandler),
], debug=True)
