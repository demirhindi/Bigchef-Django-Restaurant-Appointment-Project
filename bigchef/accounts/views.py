from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from django.contrib.auth.decorators import login_required

def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method=="POST":
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1!=password2:
            return redirect('register')

        if User.objects.filter(username=username).exists():
            return redirect('register')

        if User.objects.filter(email=email).exists():
            return redirect('register')

        user=User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
        user.save()
		
        return redirect('login')

        
    
    return render(request,"auth/register.html")
    
    


def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password1']

        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        
        return redirect('login')
    
    return render(request,'auth/login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('home')
