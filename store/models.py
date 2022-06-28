from email.headerregistry import Address
from unittest import TextTestRunner
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField, DateTimeField

# Create your models here.


class Sell(models.Model):
    itemname = models.CharField(max_length=100, null= False)
    contactnumber = models.CharField(max_length=10, null= False)
    address = models.CharField(max_length=100, null= False)
    description = models.CharField(max_length=1000, null= False)
    itemimage = models.FileField(upload_to= "static/images/items", default= "default.jpg")
    
    class Meta: 
        db_table = "item"


class Product(models.Model): 
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null =True, blank = True)
    image = models.ImageField(null = True, blank = True)
    def __str__(self):
        return self.name

    @property 
    def foo(self):
        try:
            url = self.image.url
        except:
            url= ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete = models.SET_NULL ,null = True , blank = True)
    date_ordered = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default = False)
    transaction_id = models.CharField(max_length = 100 , null = True)

    def __str__(self):
        return str(self.id)  
    
    @property 
    def get_cart_total(self):
        orderitems = self.orderitem_set.all() 
        total = sum([item.get_total for item in orderitems])
        return total 
    
    @property 
    def get_cart_items(self):
        orderitems = self.orderitem_set.all() 
        total = sum([item.one_quantity for item in orderitems])
        return total 

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL ,null= True)
    order = models.ForeignKey(Order, on_delete= models.SET_NULL, null = True)
    one_quantity = models.IntegerField(default = 1, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return str(self.product.name)
    @property 
    def get_total(self):
        total = self.product.price * self.one_quantity 
        return total 

class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete = models.SET_NULL ,null = True , blank = True)
    order = models.ForeignKey(Order, on_delete= models.SET_NULL, null = True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null = False)
    date_added = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.address 


   





