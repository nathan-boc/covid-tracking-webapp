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
        # TODO user account check
        username = self.request.get('username')
        password = self.request.get('password')
        self.response.out.write("<h1>Your username: " + username + "  Your password: " + password + "</h1>")

class SignupPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'placeholder': "PLACEHOLDER"
        }
        self.response.out.write(template.render('./templates/signup.html', template_values))

    #def post(self):
        # todo write to datastore
        #check password length and requirements
        #input full name, address, email, phone, password,

class AdminPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'placeholder': "PLACEHOLDER"
        }
        self.response.out.write(template.render('./templates/admin.html', template_values))

class HomePage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'placeholder': "PLACEHOLDER"
        }
        self.response.out.write(template.render('./templates/home.html', template_values))

app = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler=IndexPage, name='index'),
    webapp2.Route(r'/login', handler=LoginPage, name='login'),
    webapp2.Route(r'/signup', handler=SignupPage, name='signup'),
    webapp2.Route(r'/admin', handler=AdminPage, name='admin'),
    webapp2.Route(r'/home', handler=HomePage, name='home'),
    ], debug=True)

def main():
    app.run()

if __name__ == "__main__":
    main()