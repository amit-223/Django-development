from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages 

def home_view(request):
    return render(request, 'home.html/', {'message':'Welcome to Employee Management App!'})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home.html/')
        else:
            messages.error(request, 'Invalid user')
    return render(request, 'login.html/')


