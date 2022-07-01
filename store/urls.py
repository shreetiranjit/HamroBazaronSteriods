from django.urls import path 
from . import views 

urlpatterns = [
    path ('store/', views.store , name = "store"),
    path ('cart/', views.cart , name = "cart"),
    path ('checkout/', views.checkout , name = "checkout"),
    path ('sell/', views.sell , name = "sell"),
    path ('store/update_item/', views.updateItem , name = "update_item"),

]