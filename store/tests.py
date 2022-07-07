from django.test import SimpleTestCase,TestCase
from django.urls import reverse, resolve 
from store.views import *

# Create your tests here.


class TestUrls(SimpleTestCase):
    def test_cart_url(self):    
        url = reverse(cart)
        print(url)
        self.assertEquals(resolve(url).func , cart)

    def test_store_url(self):
        url = reverse(store)
        print(url)
        self.assertEquals(resolve(url).func , store)


    def test_checkout_url(self):
        url = reverse(checkout)
        print(url)
        self.assertEquals(resolve(url).func , checkout)

    def test_updateitem_url(self):
        url = reverse(updateItem)
        print(url)
        self.assertEquals(resolve(url).func , updateItem)
    
    def test_sell_url(self):
        url = reverse(sell)
        print(url)
        self.assertEquals(resolve(url).func , sell)



class testViews(TestCase): 
    def test_index(self): 
        user  = User.objects.create
