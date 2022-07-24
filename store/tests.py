from ast import arg
import json
from django.test import Client, SimpleTestCase, TestCase
from django.urls import reverse, resolve
from store.views import *
from login.models import CustomUser

# URL TESTING.

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

    def test_logout_url(self):
        url = reverse(fn_logout)
        print(url)
        self.assertEquals(resolve(url).func , fn_logout)

# VIEW TESTING.
class TestViews(TestCase):
    databases= "__all__"
    def test_index(self):

        cusUser =  CustomUser.objects.create(name='test123', password="test123")
        
        user = User.objects.create(username='test123')
        user.set_password('test123')
        user.save()
        client = Client()
        logged_in = client.login(username="test123", password="test123")
        response = client.post(reverse(sell),{
            "cususer": cusUser,
            "name": "itemname",
            "email" : "email",
            "pickup_address": "address",
            "wallet_address": "123",
            "description": "description",
            "image" :"image"
        })

        self.assertEquals(response.status_code, 302)
   

    def test_delete(self):
        cusUser =  CustomUser.objects.create(name='test123', password="test123")
        client = Client()
        c = Product.objects.create(
            userid = cusUser,
            name= "name",
            email="email",

        )
        response = client.delete(reverse(delete_listeditem, args=[1]))
        self.assertEquals(response.status_code, 302)

    def test_deletecartitem(self):

        user = User.objects.create(username='test123')
        user.set_password('test123')
        user.save()
        
        cusUser =  CustomUser.objects.create(name='test123', password="test123")
        client = Client()
        c_product = Product.objects.create(
            userid = cusUser,
            name= "name",
            email="email",
        )
        c_order = Order.objects.create(
            customer = user,
            date_ordered ="2022/01/01" ,
            complete = True,
            transaction_id = "1",


        )
        c = OrderItem.objects.create(
            product = c_product,
            order= c_order,
            one_quantity= 1,

        )
        response = client.delete(reverse(delete_cartitem, args=[1]))
        self.assertEquals(response.status_code, 302)
        

     
    def test_cart(self):
        user = User.objects.create(username='test1233')
        user.set_password('test123')
        user.save()
        
        cusUser =  CustomUser.objects.create(name='test1233', password="test123")
        client = Client()
        logged_in = client.login(username="test1233", password="test123")
        c_order = Order.objects.create(
            customer = user,
            date_ordered ="2022/01/01" ,
            complete = False,
            transaction_id = "1",
        )

        response = client.get(reverse(cart))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/cart.html')
    
    def test_editItem(self):
        user = User.objects.create(username='test1233')
        user.set_password('test123')
        user.save()
        
        cusUser =  CustomUser.objects.create(name='test1233', password="test123")
        client = Client()
        logged_in = client.login(username="test1233", password="test123")
        c_product = Product.objects.create(
            userid = cusUser,
            name= "name",
            email="email",
        )
        print(c_product.id)

        response = client.post(reverse(edit_listeditem, args=[3]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/edititem.html')
    
    
    def test_updateItem(self):
        user = User.objects.create(username='test1233')
        user.set_password('test123')
        user.save()
        
        cusUser =  CustomUser.objects.create(name='test1233', password="test123")
        client = Client()
        logged_in = client.login(username="test1233", password="test123")
        c_product = Product.objects.create(
            userid = cusUser,
            name= "name",
            email="email",
        )
        print(c_product.id)

        response = client.post(reverse(update_listeditem,args=[5]), {
            "cususer": cusUser,
            'userid': cusUser.userId,
            "name": "itemname",
            "email" : "email@2email.com",
            "pickup_address": "address",
            "wallet_address": "123",
            "description": "description",
            "image" :"image.png"
        })
        self.assertEquals(response.status_code, 302)


    def test_updatecartitem(self):
        user = User.objects.create(username='test123')
        user.set_password('test123')
        user.save()
        
        cusUser =  CustomUser.objects.create(name='test123', password="test123")
        client = Client()
        logged_in = client.login(username="test123", password="test123")

        c_product = Product.objects.create(
            userid = cusUser,
            name= "name",
            email="email",
        )
        c_order = Order.objects.create(
            customer = user,
            date_ordered ="2022/01/01" ,
            complete = True,
            transaction_id = "1",
        )
        
    
        response = client.post(
            reverse(updateItem),
            json.dumps({
                'productId': c_product.id,
                'action': True
            }),
            'json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )

     
        self.assertEquals(response.status_code, 200)



