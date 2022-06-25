from django.db import models

# Create your models here.

class userCredentials(models.Model):
    fullname = models.CharField(max_length=32, null = False)
    email = models.EmailField(max_length=80 , null =False)
    password = models.CharField(max_length=32, null = False)
    

def __str__(self):
    return self.title 