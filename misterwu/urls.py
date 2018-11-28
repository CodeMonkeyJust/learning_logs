from django.urls import path
from . import  views

urlpatterns = [
    path('misterwu/',views.home,name="home" ),
    path('user/',views.user,name="user" ),
]
