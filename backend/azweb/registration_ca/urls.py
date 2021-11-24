from django.urls import path

from . import views

app_name = "registration_ca"



urlpatterns = [
    path('',views.Index, name = 'main_website'),
    path('competitions',views.Competition, name = 'competition'),
    path('ca',views.Registration,name='index'),
    path('register', views.user_register, name = "register"),
   
]

