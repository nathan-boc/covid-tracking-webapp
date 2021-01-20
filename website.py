import webapp2
from google.appengine.ext.webapp import template

class IndexPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'placeholder': "PLACEHOLDER"
        }
        self.response.out.write(template.render('./templates/index.html', template_values))

class LoginPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'placeholder': "PLACEHOLDER"
        }
        self.response.out.write(template.render('./templates/login.html', template_values))

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        self.response.out.write("<h1>Your username: " + username + "  Your password: " + password + "</h1>")

app = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler=IndexPage, name='home'),
    webapp2.Route(r'/login', handler=LoginPage, name='login'),
    ], debug=True)

def main():
    app.run()

if __name__ == "__main__":
    main()