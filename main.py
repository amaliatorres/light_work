import webapp2
import os
import jinja2

the_jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


jinja_current_directory = "insert jinja2 environment variable here"

class Indexpage(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_environment.get_template("/templates/index.html")
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())


class Search(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_environment.get_template("/templates/search.html")
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

class Chat(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_environment.get_template("/templates/chat.html")
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', Indexpage),
    ('/search', Search),
    ('/chat', Chat)
], debug=True)
