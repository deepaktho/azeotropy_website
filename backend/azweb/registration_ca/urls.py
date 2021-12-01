from django.urls import path

from . import views

app_name = "registration_ca"



urlpatterns = [
    path('',views.Index, name = 'main_website'),
    path('competitions',views.Competition, name = 'competition'),
    path('events',views.Events, name = 'events'),
    path('about_us',views.About_us, name = 'about_us'),
    path('sponsors',views.Sponsors, name = 'sponsors'),
    path('workshop',views.Workshop, name = 'workshop'),
    path('ca',views.Registration,name='index'),
    path('register', views.user_register, name = "register"),
   
]

