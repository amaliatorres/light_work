import webapp2
import jinja2
import os


jinja_enviroment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
class IntroPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_enviroment.get_template("/templates/index.html")

        self.response.write(template.render())

class Search(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_enviroment.get_template("/templates/search.html")

        self.response.write(template.render())
class Signin(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_enviroment.get_template("/templates/sign_in.html")

        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', IntroPage),
    ('/sign_in',Signin),
    ('/search',Search)



], debug=True)
