#!/usr/bin/env python

# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START imports]
import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import db
import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]

DEFAULT_USER_NAME = 'default_user'


def user_key(user_name=DEFAULT_USER_NAME):
    """Constructs a Datastore key for a user entity.

    We use username as the key.
    """
    return ndb.Key('User', user_name)

class User(ndb.Model):
    """Sub model for representing a user."""
    Id= ndb.KeyProperty(indexed=False)
    name = ndb.StringProperty(indexed=True)
    password = ndb.IntegerProperty(indexed=False)


# [START main_page]
class MainPage(webapp2.RequestHandler):

    def changePassword(self):
        oldPassword =self.request.get("oldPassword")
        newPassword =self.request.get("newPassword")
        oldname = self.request.get('oldname')

        flag = 0
        template_values = {'error' : "true", "oldname" : oldname}
        user_query = User.query()
        user = user_query.fetch()
        #getting the record from the database
        for u in user:
            #comparing the user name from the current user name in the database
            if u.name == oldname:
                #if th user name matches then the passwords are getting compared
                #if the password matches the database gets updated 
                if str(u.password) == oldPassword :
                    template_values = {}
                    u.password = int(newPassword)
                    u.put()
                    template = JINJA_ENVIRONMENT.get_template('index.html')
                    self.response.write(template.render(template_values))
                    flag =1
                    break

        if flag ==0 :
            template = JINJA_ENVIRONMENT.get_template('password.html')
            self.response.write(template.render(template_values))
        
        

    def changeName(self):
        
        user_name =self.request.get("username")
        oldname = self.request.get("oldname")
        
        if user_name :

            user_query = User.query()
            user = user_query.fetch()
            for u in user:
                if u.name == oldname:
                    u.name = user_name
                    u.put()
                    break
            
           
            template_values = {
                
            'username' : user_name
            }

            
            template = JINJA_ENVIRONMENT.get_template('main.html')
            self.response.write(template.render(template_values))
            
        else :
            template_values = {
                
            'error' : "true"
            }
            template = JINJA_ENVIRONMENT.get_template('name.html')
            self.response.write(template.render(template_values))
        
    def post(self):
        oldname = self.request.get('oldname')

        template_values = {

            'message' : "success",
            'oldname' : oldname
            
        }

        if self.request.get('name') == 'Change Name' :
            
            template = JINJA_ENVIRONMENT.get_template('name.html')
            self.response.write(template.render(template_values))

        else :
             
            template = JINJA_ENVIRONMENT.get_template('password.html')
            self.response.write(template.render(template_values))

            
  
        
# [END main_page]


# [START loginPage]
class LoginPage (webapp2.RequestHandler):
    user1 =''
    def get(self):

        template_values = {

        
            
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

    def post(self):
        
        username = self.request.get("username")
        password = self.request.get("password")
        error = "false"
        if username  :
            self.user1 = username
            user_query = User.query()
        
            user = user_query.fetch()
            for u in user:

                print(u.name)
                print(u.password)
                if u.name == "admin" and str(u.password)=='12345':
                    print("****************")
                    template_values={'username' : username}
                    template = JINJA_ENVIRONMENT.get_template('adminHome.html')
                    self.response.write(template.render(template_values))
                    error = "true"
                    break
                elif u.name == username and str(u.password) == password :
                    template_values={'username' : username}
                    template = JINJA_ENVIRONMENT.get_template('home.html')
                    self.response.write(template.render(template_values))
                    error ="true"
                    break
                else:
                    print("inside elseeeeeeeeeeeeeeeeeee")
            
        if error =="false":
            template_values = {'error': error, "form" : "signin"}
            template = JINJA_ENVIRONMENT.get_template('index.html')
            self.response.write(template.render(template_values))

    def signup(self):
        username = self.request.get("email")
        password = self.request.get("psw")
        rpassword = self.request.get("rpsw")
        template_values = ()

        if password == rpassword:
            new_user = User()
            new_user.name= username
            new_user.password = int(password)
            new_user.put()
            template_values = {"error" : "false"}
        else:
            template_values = {"error": "true", "form" :"signup"}
        template = JINJA_ENVIRONMENT.get_template('index.html')   
        self.response.write(template.render(template_values))
            

        
# [END loginPage]




# [START app]
app = webapp2.WSGIApplication([
    webapp2.Route('/', LoginPage),
    webapp2.Route('/main', MainPage),
    webapp2.Route('/changeName', MainPage, handler_method= 'changeName'),
    webapp2.Route('/changePassword', MainPage, handler_method = 'changePassword'),
    webapp2.Route('/sign', LoginPage, handler_method = 'post'),
    webapp2.Route('/signup', LoginPage, handler_method = 'signup' ),
], debug=True)
# [END app]
