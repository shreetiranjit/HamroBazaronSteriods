from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required




# Create your views here.
        
def registerlogin(request):
    if request.method == "POST": 
        if 'name' in request.POST:
            User.objects.create_user(
                username = request.POST['name'],
                email = request.POST['email'],
                password = request.POST['password'],
            )
            return redirect ('/loginsignup')
            print(request) 
 
        elif 'username' in request.POST:
            user = authenticate(request, username = request.POST['username'], password = request.POST['password1'] )
        # print(user)
            print(request.method)
            if user is not None: 
                login(request, user) 
                return redirect('/store') 
            else: 
                return redirect('/loginsignup')
    
    else: 
        return render(request, "login/login.html")

