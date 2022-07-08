
from audioop import reverse
from unicodedata import name
from django.shortcuts import redirect, render
from pkg_resources import require
from .models import *
from login.models import *
from django.http import HttpResponseRedirect, JsonResponse
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

@login_required(login_url= "/")
def store(request): 
    context = {}
    if request.user.is_authenticated:
        customer = request.user
        order , created = Order.objects.get_or_create(customer = customer, complete = False) 
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items


        prods = Product.objects.exclude(listed_by=request.user)
        context = {'products':prods}
        return render(request, 'store/store.html',context)

from django.contrib.auth.decorators import login_required  
@login_required(login_url= "/")
def cart(request):
    context={}
    if request.user.is_authenticated:
        customer = request.user
        print(customer)
        order , created = Order.objects.get_or_create(customer = customer, complete = False) 
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        context = {'items':items , 'order':order, 'cartItems': cartItems}
    return render(request, 'store/cart.html',context) 


@login_required(login_url= "/")
def checkout(request): 
    if request.user.is_authenticated:
        customer = request.user
        order , created = Order.objects.get_or_create(customer = customer, complete = False) 
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    context = {'items':items , 'order':order,'cartItems': cartItems}   
    return render(request, 'store/cart.html',context)

@login_required(login_url= "/")

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('productId:', productId)
    customer = request.user
    product = Product.objects.get(id = productId)
    order , created = Order.objects.get_or_create(customer = customer, complete = False) 
    orderItem, created = OrderItem.objects.get_or_create(order = order , product= product)

    orderItem.save()

    return JsonResponse("Item was added" , safe = False)

@login_required(login_url= "/")
def delete_cartitem(request, product_id):
    item1= OrderItem.objects.get( product_id = product_id )
    item1.delete()
    return redirect("/cart")


# sell
@login_required(login_url= "/")

def sell(request): 

    if request.method == "POST":
 
        pro = Product(
            name = request.POST['itemname'],
            listed_by = request.user , 
            description = request.POST['description'],
            wallet_address =  request.POST['walletaddress'],
            pickup_address = request.POST['pickupaddress'],
        )
        pro.save()
        return redirect('/sell')
    else:
        return render(request, 'store/sell.html')

@login_required(login_url='/')
def fn_logout(request):
    logout(request)
    return redirect('/')