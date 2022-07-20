from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from login.forms import LoginSignupForm

# Create your views here.
        
def registerlogin(request):
    if request.method == "POST":          
            if 'name' in request.POST:
                                
                data = LoginSignupForm(request.POST)
                data.save()

                User.objects.create_user(
                    username = request.POST['name'],
                    email = request.POST['email'],
                    password = request.POST['password'],
                )
                return redirect ('/')
            elif 'username' in request.POST:    
                    user = authenticate(request, username = request.POST['username'], password = request.POST['password1'] )
                    if user is not None: 
                        login(request, user) 
                        return redirect('/store') 
                    else:
                        error = 1
                        print("error")
                        return render(request, "login/login.html" ,{'error':error})  
    else: 
        return render(request, "login/login.html")
    