import imp
from django.shortcuts import render
from .models import *
from login.models import *
from django.http import JsonResponse
import json

# Create your views here.
def store(request): 
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html',context)
    
from django.contrib.auth.decorators import login_required
@login_required(login_url= "/loginsignup")
def cart(request):
    customer = request.user
    print(customer)
    order , created = Order.objects.get_or_create(customer = customer, complete = False) 
    items = order.orderitem_set.all()
    

    context = {'items':items , 'order':order}
    return render(request, 'store/cart.html',context) 


@login_required(login_url= "/loginsignup")
def checkout(request): 
    customer = request.user
    order , created = Order.objects.get_or_create(customer = customer, complete = False) 
    items = order.orderitem_set.all()
    

    context = {'items':items , 'order':order}
    
    return render(request, 'store/checkout.html',context)

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

    if action == "add": 
        orderItem.one_quantity = (orderItem.one_quantity + 1)
    elif action == "remove":
        orderItem.one_quantity = (orderItem.one_quantity - 1)
    
    orderItem.save()

    if orderItem.one_quantity <=0 :
        orderItem.delete()

    return JsonResponse("Item was added" , safe = False)



# sell
def sell(request): 
    context = {}
    return render(request, 'store/sell.html',context)