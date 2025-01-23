from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return render(request, 'home.html/', {'message':'Welcome to Employee Management App!'})

def login_view(request):
    return render(request, 'login.html/', {'message': 'Welcome to login'})

