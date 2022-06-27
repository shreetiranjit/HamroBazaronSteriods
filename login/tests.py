from atexit import register
from django.test import SimpleTestCase,TestCase
from django.urls import reverse, resolve 
from login.views import *

# Create your tests here.


class TestUrls(SimpleTestCase):
    def test_login_url(self):    
        url = reverse(login)
        print(url)
        self.assertEquals(resolve(url).func , login)

    def test_register_url(self):
        url = reverse(register)
        print(url)
        self.assertEquals(resolve(url).func , register)


    def test_logout_url(self):
        url = reverse(logout)
        print(url)
        self.assertEquals(resolve(url).func , logout)


