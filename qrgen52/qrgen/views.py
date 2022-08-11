import email
from email.mime import image
import imp
from turtle import color
from wsgiref import validate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Create_link
from .models import Send_Mail

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
        username = request.POST.get('username')
        password = request.POST.get('pword')

        validate_user = authenticate(username=username,password=password)
        if validate_user is not None:
            login(request,validate_user)
            return redirect('home')

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

def create_link(request):
    Url=None
    if request.method=="POST":
        Url=request.POST['url']
        Color = request.POST['color']
        generate_link = Create_link(user=request.user,url=Url,color=Color)
        generate_link.save()
        

    qr_code= Create_link.objects.filter(url=Url)
    return render(request,"Qr_Pages/create_link.html",{'qr_code':qr_code})
    
def send_mail(request):
    company=None
    address = None
    if request.method=="POST":
        company=request.POST['company']
        address=request.POST['address']
        email=request.POST['email']
        #Color = request.POST['color']
        generate_link = Send_Mail(user=request.user,company=company,address=address,email=email)
        generate_link.save()
        

    qr_code= Send_Mail.objects.filter(company=company)
    return render(request,"Qr_Pages/email.html",{'qr_code':qr_code})
    

