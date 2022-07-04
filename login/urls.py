from django.urls import path
from login import views
urlpatterns = [
    path('', views.registerlogin),
    # path("/create", views.create),
    # path("/save",views.saveFn),
    # path("/edit/<int:id>", views.edit),
    # path("/update/<int:id>",views.update),
    # path("/delete/<int:id>", views.delete)

    
]