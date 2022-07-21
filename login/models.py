from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.

class CustomUser(models.Model):
    userId = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=32, null = False)
    email = models.EmailField(max_length=80 , null =False, unique=True)
    password = models.CharField(max_length=32, null = False)
    cpassword = models.CharField(max_length=32, null = False, default= "null")


def __str__(self):
    return self.title 