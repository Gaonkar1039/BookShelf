from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
# Create your views here.
def index(request):
    if request.user.is_anonymous:

        return redirect("/login")

    return render(request, "index.html")

def loginuser(request):
    print("hello")
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')



        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html")


    return render(request, "login.html")

def logoutuser(request):
    logout(request)
    return redirect("/login")
    
def about(request):
    return render(request, "about.html")
def navigation(request):
    return render(request, "navbar.html")
# def services(request):
#     return render(request, "index.html")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('desc')
        contact = Contact(name = name,phone = phone, email = email, description=description, date = datetime.today())
        contact.save()
        messages.success(request,'Your details has been sent')

    return render(request, "contact.html")