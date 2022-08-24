from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name = 'home'),
    path("about", views.about, name = 'about'),
    path("contact", views.contact, name = 'contact'),
    path("login", views.loginuser, name = "login"),
    path("logout", views.logoutuser, name="logout" ),
    path("navbar", views.navigation, name="navbar" )
    # path("services", views.services, name = 'services')

]