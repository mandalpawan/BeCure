from unicodedata import name
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('service/',views.service,name='service'),
    path('sin_up/',views.sin_up,name='sin_up'),
    path('logout/',views.logout,name='logout'),
    path("login/",views.login,name="login"),
    path("about/",views.about,name="about"),
    path("booking/",views.booking,name="booking"),
    path("appointment/",views.appointment,name='appointment'),
    path("subs/",views.subs,name='subs'),
]