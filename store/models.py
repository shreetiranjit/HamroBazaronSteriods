from distutils.command.upload import upload
from email.headerregistry import Address
from email.policy import default
from tkinter import CASCADE
from unittest import TextTestRunner
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField, DateTimeField

from login.models import CustomUser

# Create your models here.
class Product(models.Model): 
    id = models.AutoField(primary_key=True)
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




