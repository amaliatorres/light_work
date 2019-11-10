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

app = webapp2.WSGIApplication([
    ('/', IntroPage)

], debug=True)
