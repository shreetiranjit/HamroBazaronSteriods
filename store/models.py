from distutils.command.upload import upload
from email.headerregistry import Address
from email.policy import default
from unittest import TextTestRunner
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField, DateTimeField

from login.models import CustomUser

# Create your models here.
class Product(models.Model): 
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "static/images/items" )
    userid = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    email = models.EmailField(max_length=200)
    wallet_address = models.CharField(max_length= 42 , null = True)
    pickup_address = models.CharField(max_length= 200, null = False)
    description = models.CharField(max_length= 200,null= False )
    is_reserved = models.BooleanField(default=False )
    reserved_by = models.CharField(default='No one', max_length=100)
    def __str__(self):
        return self.name

    def lister_mail(self):
        return (self.email.email)

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete = models.SET_NULL ,null = True , blank = True)
    date_ordered = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default = False)
    transaction_id = models.CharField(max_length = 100 , null = True)

    def __str__(self):
        return str(self.id)  
    
    @property 
    def get_cart_items(self):
        print("get cart")
        orderitems = self.orderitem_set.all() 
        print("get cart orderitems : ", orderitems)
        # total = sum([item.one_quantity for item in orderitems])
        totalEg = 0
        for i in orderitems:
            totalEg += i.one_quantity 
        # print("Total: ",total)
        return totalEg

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE ,null= True)
    order = models.ForeignKey(Order, unique=True, on_delete= models.CASCADE, null = True)
    one_quantity = models.IntegerField(default = 1, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return str(self.product.name)
    





