from django.urls import path 
from . import views 

urlpatterns = [
    path ('store/', views.store , name = "store"),
    path ('cart/', views.cart , name = "cart"),
    path ('checkout/', views.checkout , name = "checkout"),
    path ('sell/', views.sell , name = "sell"),
    path ('store/store/update_item/', views.updateItem , name = "update_item"),
    path('logout/', views.fn_logout, name='logout'),
    path('deletecartitem/<int:product_id>', views.delete_cartitem, name = "deleteCartItem")

]