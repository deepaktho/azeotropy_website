from django.urls import path

from . import views

app_name = "registration_ca"



urlpatterns = [
    path('ca',views.Registration,name='index'),
    path('register', views.user_register, name = "register"),
   
]

