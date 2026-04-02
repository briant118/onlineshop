from django.shortcuts import render, redirect

def login(request):
    return render(request, 'authentication/login.html',{})

def logout(request):
    return redirect('login')

def register(request):
    return render(request, 'userprofile/register.html')


