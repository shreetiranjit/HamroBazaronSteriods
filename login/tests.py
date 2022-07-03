from atexit import register
from django.test import SimpleTestCase,TestCase
from django.urls import reverse, resolve 
from login.views import *

# Create your tests here.


class TestUrls(SimpleTestCase):
    def test_login_url(self):    
        url = reverse(registerlogin)
        print(url)
        self.assertEquals(resolve(url).func , registerlogin)

    def test_register_url(self):
        url = reverse(registerlogin)
        print(url)
        self.assertEquals(resolve(url).func , registerlogin)


    


