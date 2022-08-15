
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Text_Message,Contact_Details
from .models import Send_Mail
from PIL import Image
import os
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



def convert_to_jpeg(path):
    image = Image.open(path)
    rgb_image= image.convert('RGB')
    jpeg_image = rgb_image.save(path.replace('.png','.jpeg'), 'JPEG')
    return path.replace('.png','.jpeg'),os.path.basename(path.replace('.png','.jpeg'))

def convert_to_pdf(path):
    image = Image.open(path)
    rgb_image= image.convert('RGB')
    pdf_image = rgb_image.save(path.replace('.png','.pdf'), 'PDF')
    return path.replace('.png','.pdf'),os.path.basename(path.replace('.png','.pdf'))
    
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
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pword')

        validate_user = authenticate(username=username,password=password)
        if validate_user is not None:
            login(request,validate_user)
            return redirect('profile')

        else:
            messages.error(request,'Wrong User Details or User does not exist')
            return redirect('login')

    return render(request, 'accounts/login.html', {})
@login_required
def profile(request):
    return render(request, 'profile.html', {})

@login_required
def contactpage(request):
    return render(request, 'contactus.html', {})

def aboutpage(request):
    return render(request, 'about_us.html', {})

def faqpage(request):
    return render(request, 'faqs.html', {})

def helppage(request):
    return render(request, 'help.html', {})
@login_required

@login_required
def send_mail(request):
    company=None
    address = None
    if request.method=="POST":
        company=request.POST['company']
        address=request.POST['address']
        email=request.POST['email']
        Color = request.POST['color']
        generate_link = Send_Mail(user=request.user,company=company,address=address,email=email,color=Color)
        generate_link.save()
        return redirect('download_mail')

    qr_code= Send_Mail.objects.filter(user=request.user)
    return render(request,"Qr_Pages/email.html",{'qr_code':qr_code})
    
@login_required
def contact_details(request):
    contact_name=None
    phoneNumber=None
    if request.method == "POST":
        contact_name = request.POST['contact_name']
        company = request.POST['company']
        email= request.POST['email']
        website= request.POST['website']
        address = request.POST['address']
        phoneNumber = request.POST['number']
        generate_link = Contact_Details(
        user=request.user,contact_name=contact_name,number=phoneNumber,email=email,website=website, company=company, address=address)
        generate_link.save()
        return redirect('download_contact')
    
    qr_code= Contact_Details.objects.filter(user=request.user)
    return render(request, 'Qr_Pages/contact.html', {'qr_code':qr_code})

@login_required
def text_message(request):
    number=None
    text = None
    if request.method=="POST":
        number=request.POST['number']
        text=request.POST['text']
        Color = request.POST['color']
        generate_link = Text_Message(user=request.user,number=number,text=text,color=Color)
        generate_link.save()
        return redirect('download_text')

    qr_code= Text_Message.objects.filter(user=request.user)
    return render(request, 'Qr_Pages/text_message.html', {'qr_code':qr_code})

@login_required
def image_upload(request):
    
    return render(request, 'Qr_Pages/image_upload.html', {})

@login_required
def video(request):
    return render(request, 'Qr_Pages/video_upload.html', {})

@login_required
def audio(request):
    return render(request, 'Qr_Pages/audio_file.html', {})



@login_required
def download_mail(request):
    latest_qr_code = Send_Mail.objects.filter(user=request.user).order_by('-id')[0]
    
    return render(request, 'download_mail.html', {'latest_qr_code':latest_qr_code})
@login_required
def download_contact(request):
    latest_contact_qr_code = Contact_Details.objects.filter(user=request.user).order_by('-id')[0]
    
    return render(request, 'download_contact.html', {'latest_contact_qr_code':latest_contact_qr_code})
@login_required
def download_text_message(request):
    latest_message_qr_code = Text_Message.objects.filter(user=request.user).order_by('-id')[0]
    
    return render(request, 'download_message.html', {'latest_message_qr_code':latest_message_qr_code})


def download_link_png(request,pk):
    obj= get_object_or_404(Create_link.objects.filter(user=request.user),pk=pk)
    filepath = obj.qr_image.path
    filename= obj.qr_image.name
    response=HttpResponse(open(filepath,'rb').read(),content_type='image/png')
    response['Content-Disposition']= f'attachment; filename=%s' % filename
    return response
    
def download_link_pdf(request,pk):
    obj= get_object_or_404(Create_link.objects.filter(user=request.user),pk=pk)
    filepath,filename = convert_to_pdf(obj.qr_image.path)
    response=HttpResponse(open(filepath,'rb').read(),content_type='application/pdf')
    response['Content-Disposition']= 'attachment; filename=%s' % filename 
    return response

def download_link_jpeg(request,pk):
    obj= get_object_or_404(Create_link.objects.filter(user=request.user),pk=pk)
    filepath,filename = convert_to_jpeg(obj.qr_image.path)
    response=HttpResponse(open(filepath,'rb').read(),content_type='image/jpeg')
    response['Content-Disposition']= 'attachment; filename= %s' % filename 
    return response

def download_mail_png(request,pk):
    obj= get_object_or_404(Send_Mail.objects.filter(user=request.user),pk=pk)
    filepath = obj.Qr_Image.path
    filename= obj.Qr_Image.name
    response=HttpResponse(open(filepath,'rb').read(),content_type='image/png')
    response['Content-Disposition']= f'attachment; filename=%s' % filename
    return response

def download_mail_pdf(request,pk):
    obj= get_object_or_404(Send_Mail.objects.filter(user=request.user),pk=pk)
    filepath,filename = convert_to_pdf(obj.Qr_Image.path)
    response=HttpResponse(open(filepath,'rb').read(),content_type='application/pdf')
    response['Content-Disposition']= 'attachment; filename=%s' % filename 
    return response

def download_mail_jpeg(request,pk):
    obj= get_object_or_404(Send_Mail.objects.filter(user=request.user),pk=pk)
    filepath,filename = convert_to_jpeg(obj.Qr_Image.path)
    response=HttpResponse(open(filepath,'rb').read(),content_type='image/jpeg')
    response['Content-Disposition']= 'attachment; filename= %s' % filename 
    return response

def download_contact_png(request,pk):
    obj= get_object_or_404(Contact_Details.objects.filter(user=request.user),pk=pk)
    filepath = obj.qr_Image.path
    filename= obj.qr_Image.name
    response=HttpResponse(open(filepath,'rb').read(),content_type='image/png')
    response['Content-Disposition']= f'attachment; filename=%s' % filename
    return response

def download_contact_pdf(request,pk):
    obj= get_object_or_404(Contact_Details.objects.filter(user=request.user),pk=pk)
    filepath,filename = convert_to_pdf(obj.qr_Image.path)
    response=HttpResponse(open(filepath,'rb').read(),content_type='application/pdf')
    response['Content-Disposition']= 'attachment; filename=%s' % filename 
    return response

def download_contact_jpeg(request,pk):
    obj= get_object_or_404(Contact_Details.objects.filter(user=request.user),pk=pk)
    filepath,filename = convert_to_jpeg(obj.qr_Image.path)
    response=HttpResponse(open(filepath,'rb').read(),content_type='image/jpeg')
    response['Content-Disposition']= 'attachment; filename= %s' % filename 
    return response

def download_message_png(request,pk):
    obj= get_object_or_404(Text_Message.objects.filter(user=request.user),pk=pk)
    filepath = obj.Qr_image.path
    filename= obj.Qr_image.name
    response=HttpResponse(open(filepath,'rb').read(),content_type='image/png')
    response['Content-Disposition']= f'attachment; filename=%s' % filename
    return response

def download_message_pdf(request,pk):
    obj= get_object_or_404(Text_Message.objects.filter(user=request.user),pk=pk)
    filepath,filename = convert_to_pdf(obj.Qr_image.path)
    response=HttpResponse(open(filepath,'rb').read(),content_type='application/pdf')
    response['Content-Disposition']= 'attachment; filename=%s' % filename 
    return response

def download_message_jpeg(request,pk):
    obj= get_object_or_404(Text_Message.objects.filter(user=request.user),pk=pk)
    filepath,filename = convert_to_jpeg(obj.Qr_image.path)
    response=HttpResponse(open(filepath,'rb').read(),content_type='image/jpeg')
    response['Content-Disposition']= 'attachment; filename= %s' % filename 
    return response

def logout_view(request):
    logout(request)
    return redirect('login')
