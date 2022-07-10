from distutils.command.upload import upload
from email.headerregistry import Address
from email.policy import default
from unittest import TextTestRunner
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField, DateTimeField

# Create your models here.




class Product(models.Model): 
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "static/images/items" , default="default.jpg")
    listed_by = models.ForeignKey(User, null=False,  on_delete = models.CASCADE)
    wallet_address = models.CharField(max_length= 42 , null = True, default="")
    pickup_address = models.CharField(max_length= 200, null = False, default="")
    description = models.CharField(max_length= 200,null= False , default= "")
    def __str__(self):
        return self.name

    def lister_mail(self):
        return (self.listed_by.email)

    

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete = models.SET_NULL ,null = True , blank = True)
    date_ordered = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default = False)
    transaction_id = models.CharField(max_length = 100 , null = True)

    def __str__(self):
        return str(self.id)  
    
    @property
    def shipping(self):
        shipping= False 
        Orderitems = self.orderitem_set.all()
        for i in Orderitems:
            if i.product.physical == False: 
                shipping = True 
        return shipping 
    
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


   





