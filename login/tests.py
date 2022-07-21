from django.test import Client, SimpleTestCase,TestCase
from django.urls import reverse, resolve 
from login.views import *

# URL TESTING


class TestUrls(SimpleTestCase):
    def test_login_url(self):    
        url = reverse(registerlogin)
        print(url)
        self.assertEquals(resolve(url).func , registerlogin)

    def test_register_url(self):
        url = reverse(registerlogin)
        print(url)
        self.assertEquals(resolve(url).func , registerlogin)



# VIEW TESTING.
class TestViews(TestCase):

    def test_index(self):
        #create new user with username and password
        user = User.objects.create(username='test123')
        user.set_password('test123')
        user.save()

        # To login 
        client = Client()
        logged_in = client.login(username="test123", password="test123")
        response = client.get(reverse(registerlogin))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "login/login.html")

   
