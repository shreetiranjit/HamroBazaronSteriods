
from django.shortcuts import redirect, render
from .models import *
from login.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from store.forms import ProductForm
from django.contrib.auth.decorators import login_required  

# Create your views here.

@login_required(login_url= "/")
def store(request): 
    r = Product.objects.filter(reserved_by = request.user.username)
    rescount = 0
    for res in r:
        rescount +=1
    context = {}
    if request.user.is_authenticated:
        curUser = request.user
        email = curUser.email
        cusUser = CustomUser.objects.get(email= email) 
        uId = cusUser.userId
        print(uId)
        prods = Product.objects.exclude(userid_id =uId)
        context = {'products':prods ,
         'rescount':rescount,
        }
        return render(request, 'store/store.html',context)

@login_required(login_url= "/")
def sell(request): 
    curUser = request.user
    email = curUser.email 
    cusUser = CustomUser.objects.get(email= email) 
    uId = cusUser.userId
    if request.method == "POST" :
        r = Product.objects.filter(reserved_by = request.user.username)
        rescount = 0
        for res in r:
            rescount +=1
        pro = Product(
            name = request.POST['name'],
            email = request.POST['email'] , 
            userid_id = uId,
            description = request.POST['description'],
            wallet_address =  request.POST['wallet_address'],
            pickup_address = request.POST['pickup_address'],
            image = request.FILES.get("image"),
        )
        pro.save()
        return redirect('/sell' )
    else:
        return render(request, 'store/sell.html', {'rescount':rescount})


@login_required(login_url= "/")
def delete_listeditem(request, id):
    item2= Product.objects.get( id = id )
    item2.delete()
    
    return redirect("/myprofile")

@login_required(login_url= "/")
def edit_listeditem(request, id):
    item2= Product.objects.get( id = id ) 
    print(item2)
    return render(request, "store/edititem.html" , {"item2":item2})

@login_required(login_url= "/")
def update_listeditem(request, id):
    item2= Product.objects.get( id = id )

    if request.method=="POST":
        form = ProductForm({
        'userid':request.user.id,
        'description':request.POST['description'],
        'name': request.POST['name'],
        'email':request.POST['email'],
        'wallet_address':request.POST['wallet_address'],
        'pickup_address':request.POST['pickup_address'],
        'reserved_by': 'No one'
         },
        request.FILES, instance= item2)
        if form.is_valid():
            form.save()
            return redirect("/myprofile")

        else:
            print(form.errors.as_data)
            return redirect("/myprofile")

@login_required(login_url= "/")
def reserve(request, pid):
    print('reserve bhayo yayy')

    pro = Product.objects.get(id = pid)
    pro.is_reserved = 1
    pro.reserved_by = request.user.username
    pro.save()
    return redirect('/store')



@login_required(login_url= "/")
def unreserve(request, pid):
    pro = Product.objects.get(id = pid)
    pro.is_reserved = 0
    pro.reserved_by = ""
    pro.save()
    return redirect('/store')

@login_required
def edit_profile(request):
    cuser = CustomUser.objects.get(userId = request.user.id)
    if request.method=="POST":
        request.user.email = request.POST['email']
        cuser.email = request.POST['email']
        cuser.save()
        request.user.save()
        return redirect('myprofile')
    return render(request,'profile/editprofile.html')

@login_required(login_url='/')
def myprofile(request): 
    r = Product.objects.filter(reserved_by = request.user.username)
    rescount = 0
    for res in r:
        rescount +=1    
    if request.user.is_authenticated:
        curUser = request.user
        email = curUser.email
        cusUser = CustomUser.objects.get(email= email) 
        uId = cusUser.userId
        productlist = Product.objects.filter(userid_id = uId )
        revPro = Product.objects.filter(reserved_by = request.user.username)

        print(productlist)
        context = {'products':productlist, 'uId':uId, 'reserves':revPro , 'rescount': rescount}
        print(context)
        return render(request, 'store/myProfile.html', context)





@login_required(login_url='/')
def fn_logout(request):
    logout(request)
    return redirect('/')