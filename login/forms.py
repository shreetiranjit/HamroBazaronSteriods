from django import forms 
from login.models import CustomUser
from django.contrib.auth.models import User

class LoginSignupForm(forms.ModelForm):
    class Meta :
        model = CustomUser
        fields = "__all__" 
    
    

    
    