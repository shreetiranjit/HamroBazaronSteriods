from django import forms 
from login.models import customUser
from django.contrib.auth.models import User

class LoginSignupForm(forms.ModelForm):
    class Meta :
        model = customUser
        fields = "__all__" 
    
    

    
    