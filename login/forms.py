from django import forms 
from login.models import signup
class LoginSignupForm(forms.ModelForm):
    class Meta :
        model = signup
        fields = "__all__" 
        