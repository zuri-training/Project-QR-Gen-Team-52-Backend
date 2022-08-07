import email
from wsgiref import validate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'index.html', {})

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')

        if len(password) < 8:
            messages.error(request,'Password must be atleast 8 characters')
            return redirect('register')

        get_all_users_by_username = User.objects.filter(username=username)
        if get_all_users_by_username:
             messages.error(request,'Username already exist, Try Another')
             return redirect('register')

        get_all_users_by_email = User.objects.filter(email=email)
        if get_all_users_by_email:
             messages.error(request,'Email already exist, Try Another')
             return redirect('register')

        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        
        messages.success(request, 'User succesfully created')
        return redirect('login')

    return render(request, 'accounts/signup.html', {})

def loginpage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pword')

        validate_user = authenticate(email=email,password=password)
        if validate_user is not None:
            login(request,validate_user)
            return redirect('home-page')

        else:
            messages.error(request,'Wrong User Details or User does not exist')
            return redirect('login')

    return render(request, 'accounts/login.html', {})


def contactpage(request):
    return render(request, 'contactus.html', {})

def aboutpage(request):
    return render(request, 'index.html', {})

def faqpage(request):
    return render(request, 'index.html', {})
