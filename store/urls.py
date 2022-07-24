from django.urls import path 
from . import views 

urlpatterns = [
    path ('store/', views.store , name = "store"),
    path ('sell/', views.sell , name = "sell"),
    path ('reserve/<int:pid>', views.reserve , name = "reserve"),
    path ('unreserve/<int:pid>', views.unreserve , name = "unreserve"),
    path('myprofile/', views.myprofile , name = "myprofile"),
    path('logout/', views.fn_logout, name='logout'),
    path('edit_profile/' , views.edit_profile, name='editprofile'),
    path('deletelisteditem/<int:id>', views.delete_listeditem, name = "deleteListedItem"),
    path('myprofile/editlisteditem/<int:id>', views.edit_listeditem, name = "editListedItem"),
    path('updatelisteditem/<int:id>', views.update_listeditem, name = "updateListedItem"),
]