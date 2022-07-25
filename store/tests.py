from ast import arg
import email
import json
from django.test import Client, SimpleTestCase, TestCase
from django.urls import reverse, resolve
from store.views import *
from login.models import CustomUser

# URL TESTING.

# class TestUrls(SimpleTestCase):
    # def test_reserve_url(self):
    #     url = reverse(reserve, args=[1])
    #     print(url)
    #     self.assertEquals(resolve(url).func , reserve)

    # def test_store_url(self):
    #     url = reverse(store)
    #     print(url)
    #     self.assertEquals(resolve(url).func , store)


    # def test_reserve_url(self):
    #     url = reverse(delete_listeditem, args = [1])
    #     print(url)
    #     self.assertEquals(resolve(url).func , delete_listeditem)

    # def test_updateitem_url(self):
    #     url = reverse(edit_profile)
    #     print(url)
    #     self.assertEquals(resolve(url).func , edit_profile)

    # def test_sell_url(self):
    #     url = reverse(sell)
    #     print(url)
    #     self.assertEquals(resolve(url).func , sell)

    # def test_logout_url(self):
    #     url = reverse(fn_logout)
    #     print(url)
    #     self.assertEquals(resolve(url).func , fn_logout)

# VIEW TESTING.
# class TestViews(TestCase):
#     databases= "__all__"
    # def test_index(self):
    #     cusUser =  CustomUser.objects.create(name='test123', password="test123")
    #     user = User.objects.create(username='test123')
    #     user.set_password('test123')
    #     user.save()
    #     client = Client()
    #     logged_in = client.login(username="test123", password="test123")
    #     response = client.post(reverse(sell),{
    #         "cususer": cusUser,
    #         "name": "itemname",
    #         "email" : "email",
    #         "pickup_address": "address",
    #         "wallet_address": "123",
    #         "description": "description",
    #         "image" :"image"
    #     })

    #     self.assertEquals(response.status_code, 302)
   

    # def test_delete(self):
    #     cusUser =  CustomUser.objects.create(name='test123', password="test123")
    #     client = Client()
    #     c = Product.objects.create(
    #         userid = cusUser,
    #         name= "name",
    #         email="email",

    #     )
    #     response = client.delete(reverse(delete_listeditem, args=[1]))
    #     self.assertEquals(response.status_code, 302)

    # def test_unreserveitem(self):

    #     user = User.objects.create(username='test123')
    #     user.set_password('test123')
    #     user.save()
        
    #     cusUser =  CustomUser.objects.create(name='test123', password="test123")
    #     client = Client()
    #     c_product = Product.objects.create(
    #         userid = cusUser,
    #         name= "name",
    #         email="email",
    #     )
        
    #     response = client.delete(reverse(unreserve, args=[1]))
    #     self.assertEquals(response.status_code, 302)
             
    # def test_reserve(self):
    #     user = User.objects.create(username='test1233')
    #     user.set_password('test123')
    #     user.save()
        
    #     cusUser =  CustomUser.objects.create(name='test1233', password="test123")
    #     client = Client()
    #     logged_in = client.login(username="test1233", password="test123")
    #     c = Product.objects.create(
    #         userid = cusUser,
    #         name= "name",
    #         email="email",

    #     )
    #     response = client.get(reverse(reserve ,args= [1]))
    #     self.assertEquals(response.status_code, 302)
    
    # def test_editItem(self):
    #     user = User.objects.create(username='test1233')
    #     user.set_password('test123')
    #     user.save()
        
    #     cusUser =  CustomUser.objects.create(name='test1233', password="test123")
    #     client = Client()
    #     logged_in = client.login(username="test1233", password="test123")
    #     c_product = Product.objects.create(
    #         userid = cusUser,
    #         name= "name",
    #         email="email",
    #         wallet_address= "1234567",
    #         pickup_address = "asd",
    #         is_reserved = False,
    #         reserved_by = "No onr"
    #     )
    #     print(c_product.id)

    #     response = client.post(reverse(edit_listeditem, args=[1]))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'store/edititem.html')
    
    # def test_updateItem(self):
    #     user = User.objects.create(username='test1233')
    #     user.set_password('test123')
    #     user.save()
        
    #     cusUser =  CustomUser.objects.create(name='test1233', password="test123")
    #     client = Client()
    #     logged_in = client.login(username="test1233", password="test123")
    #     c_product = Product.objects.create(
    #         userid = cusUser,
    #         name= "name",
    #         email="email",
    #     )
    #     print(c_product.id)

    #     response = client.post(reverse(update_listeditem,args=[1]), {
    #         "cususer": cusUser,
    #         'userid': cusUser.userId,
    #         "name": "itemname",
    #         "email" : "email@2email.com",
    #         "pickup_address": "address",
    #         "wallet_address": "123",
    #         "description": "description",
    #         "image" :"image.png"
    #     })
    #     self.assertEquals(response.status_code, 302)
    
    
    # def test_updateProfile(self):
    #     user = User.objects.create(username='test1233')
    #     user.set_password('test123')
    #     user.save()
        
    #     cusUser =  CustomUser.objects.create(name='test1233', password="test123")
    #     client = Client()
    #     logged_in = client.login(username="test1233", password="test123")
        

    #     response = client.post(reverse(edit_profile), {
    #         "cususer": cusUser,
    #         'userid': cusUser.userId,
    #         "name": "itemname",
    #         "email" : "email@2email.com",
    #         "pickup_address": "address",
    #         "wallet_address": "123",
    #         "description": "description",
    #         "image" :"image.png"
    #     })
    #     self.assertEquals(response.status_code, 302)

    
        

        



