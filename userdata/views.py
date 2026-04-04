from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password

from .models import userdata as Userdata


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        userchecker = authenticate(request, username=username, password=password)
        if userchecker is not None:
            auth_login(request, userchecker)
            return redirect('home')
        messages.error(request, 'Invalid username or password')
    return render(request, 'home.html', {})


def logout(request):
    auth_logout(request)
    return redirect('user_login')


def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name', '')
        lastname = request.POST.get('last_name', '')
        username = request.POST.get('username', '')
        password = make_password(request.POST.get('password', ''))

        Userdata.objects.create(
            firstname=firstname,
            lastname=lastname,
            username=username,
            password=password,
        )
        return redirect('user_login')
    return render(request, 'userprofile/register.html')