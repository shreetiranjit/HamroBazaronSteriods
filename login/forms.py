from django import forms 
from login.models import signup
from django.contrib.auth.models import User

class LoginSignupForm(forms.ModelForm):
    class Meta :
        model = signup
        fields = "__all__" 
    
    

    
    