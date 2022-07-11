from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required

from login.forms import LoginSignupForm




# Create your views here.
        
def registerlogin(request):
    
        if request.method == "POST": 
            # form = LoginSignupForm(request.POST)
            # if form.is_valid():
                if 'name' in request.POST:
                    User.objects.create_user(
                        username = request.POST['name'],
                        email = request.POST['email'],
                        password = request.POST['password'],
                    )
                    return redirect ('/')
                    print(request) 
        
                elif 'username' in request.POST:
                    user = authenticate(request, username = request.POST['username'], password = request.POST['password1'] )
                
                    print(request.method)
                    if user is not None: 
                        login(request, user) 
                        return redirect('/store') 
                    else: 
                        return redirect('/')
            # else:
            #     password1 = form.data['password']
            #     password2 = form.data['cpassword']
            #     email = form.data['email']
            #     for msg in form.errors.as_data():
            #         if msg == 'email':
            #             messages.error(request, f"Declared {email} is not valid")
            #         if msg == 'password2' and password1 == password2:
            #             messages.error(request, f"Selected password: {password1} is not strong enough")
            #         elif msg == 'password2' and password1 != password2:
            #             messages.error(request, f"Password: '{password1}' and Confirmation Password: '{password2}' do not match")
            
        else: 
            return render(request, "login/login.html")
    