import webapp2
import os
import jinja2

the_jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


jinja_current_directory = "insert jinja2 environment variable here"

class Main(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_environment.get_template("/templates/index.html")
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

class Landing(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_environment.get_template("/templates/landing.html")
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

class Search(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_environment.get_template("/templates/search.html")
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', Landing),
    ('/index', Main),
    ('/search', Search)
], debug=True)
