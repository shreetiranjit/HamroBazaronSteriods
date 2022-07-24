import json
from django.shortcuts import redirect, render
from .models import *
from login.models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
from store.forms import ProductForm
from django.contrib.auth.decorators import login_required  

# Create your views here.


@login_required(login_url= "/")
def store(request): 
    context = {}
    if request.user.is_authenticated:
        customer = request.user
        order , created = Order.objects.get_or_create(customer = customer, complete = False) 
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        curUser = request.user
        email = curUser.email
        cusUser = CustomUser.objects.get(email= email) 
        uId = cusUser.userId
        print(uId)
        prods = Product.objects.exclude(userid_id =uId)
        context = {'products':prods ,
        'cartItems': cartItems
        }
        return render(request, 'store/store.html',context)

@login_required(login_url= "/")
def cart(request):
    context={}
    print("entered")
    if request.user.is_authenticated:
        print("Auth")
        customer = request.user
        print(customer)
        order  = Order.objects.get(customer = customer, complete = False) 
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        print(cartItems)
        print(order)
        print("itemss",items)
        context = {'items':items , 'order':order, 'cartItems': cartItems}
    return render(request, 'store/cart.html',context) 


@login_required(login_url= "/")
def checkout(request): 
    if request.user.is_authenticated:
        customer = request.user
        order ,created = Order.objects.get_or_create(customer = customer, complete = False) 
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    context = {'items':items , 'order':order,'cartItems': cartItems}   
    return render(request, 'store/cart.html',context)

@login_required(login_url= "/")
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user
    product = Product.objects.get(id = productId)
    product.reserved_by = request.user.username
    product.is_reserved = True
    product.save()
    try:
       order = Order.objects.get(customer=customer)
       print("uCart gotten")
    except Order.DoesNotExist:
       obj = Order.objects.create(customer=customer)
       obj.save()
       print("uCart new made")

    orderItem, created = OrderItem.objects.get_or_create(order = order , product= product)

    orderItem.save()
    print("saved")
    return JsonResponse("Item was added" , safe = False)

@login_required(login_url= "/")
def delete_cartitem(request, product_id):
    item1= OrderItem.objects.get( product_id = product_id )
    item1.delete()
    prod = Product.objects.get(id=product_id)
    prod.is_reserved= False
    prod.reserved_by = ""
    prod.save()
    return redirect("/cart")

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
def sell(request): 
    curUser = request.user
    email = curUser.email 
    cusUser = CustomUser.objects.get(email= email) 
    uId = cusUser.userId
    if request.method == "POST" :
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
        return render(request, 'store/sell.html')

@login_required(login_url='/')
def myprofile(request): 
    if request.user.is_authenticated:
        curUser = request.user
        email = curUser.email
        cusUser = CustomUser.objects.get(email= email) 
        uId = cusUser.userId
        productlist = Product.objects.filter(userid_id = uId )
        print(productlist)
        context = {'products':productlist, 'uId':uId}
        print(context)
        return render(request, 'store/myProfile.html', context)

@login_required(login_url='/')
def fn_logout(request):
    logout(request)
    return redirect('/')