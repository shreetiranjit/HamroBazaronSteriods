from django.urls import path 
from . import views 

urlpatterns = [
    path ('store/', views.store , name = "store"),
    path ('cart/', views.cart , name = "cart"),
    path ('checkout/', views.checkout , name = "checkout"),
    path ('sell/', views.sell , name = "sell"),
    path ('update_item/', views.updateItem , name = "update_item"),
    path('myprofile/', views.myprofile , name = "myprofile"),
    path('logout/', views.fn_logout, name='logout'),
    path('deletecartitem/<int:product_id>', views.delete_cartitem, name = "deleteCartItem"),
    path('deletelisteditem/<int:id>', views.delete_listeditem, name = "deleteListedItem"),
    path('myprofile/editlisteditem/<int:id>', views.edit_listeditem, name = "editListedItem"),
    path('myprofile/editlisteditem/myprofile/updatelisteditem/<int:id>', views.update_listeditem, name = "updateListedItem"),

]