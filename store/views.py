
from django.shortcuts import render
from .models import *
from login.models import *
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def store(request): 
    if request.user.is_authenticated:
        customer = request.user
        order , created = Order.objects.get_or_create(customer = customer, complete = False) 
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items


    products = Product.objects.all()
    context = {'products':products, 'cartItems': cartItems}
    return render(request, 'store/store.html',context)

from django.contrib.auth.decorators import login_required  
@login_required(login_url= "/loginsignup")
def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        print(customer)
        order , created = Order.objects.get_or_create(customer = customer, complete = False) 
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    

    context = {'items':items , 'order':order, 'cartItems': cartItems}
    return render(request, 'store/cart.html',context) 


@login_required(login_url= "/loginsignup")
def checkout(request): 
    if request.user.is_authenticated:
        customer = request.user
        order , created = Order.objects.get_or_create(customer = customer, complete = False) 
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    context = {'items':items , 'order':order,'cartItems': cartItems}   
    return render(request, 'store/cart.html',context)

@login_required(login_url= "/loginsignup")

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



# sell
@login_required(login_url= "/loginsignup")

def sell(request): 
    context = {}
    return render(request, 'store/sell.html',context)
@login_required(login_url='/loginsignup')
def fn_logout():
    logout()