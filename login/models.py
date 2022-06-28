from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField

# Create your models here.

class signup(models.Model):
    name = models.CharField(max_length=32, null = False)
    email = models.EmailField(max_length=80 , null =False)
    password = models.CharField(max_length=32, null = False)


def __str__(self):
    return self.title 