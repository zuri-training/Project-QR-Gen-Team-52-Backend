
from django.db import models
import qrcode

from io import BytesIO
from django.core.files import File
from django.contrib.auth.models import User

# Create your models here.
import random
class Create_link(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    url=models.URLField()
    qr_image=models.ImageField(upload_to='qrcode',blank=True)
    color=models.CharField(max_length=40, default='black')

    def __str__(self):
        return self.url

    def save(self,*args,**kwargs):
      qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
      )  
      qr.add_data(self.url)
      qr.make(fit=True)
      qrcode_img= qr.make_image(fill_color=self.color)
      buffer=BytesIO()
      qrcode_img.save(buffer,format='PNG')
      self.qr_image.save('myqr.png',File(buffer),save=False)
      super().save(*args,**kwargs)


class Send_Mail(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    company=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.CharField(max_length=100)
    Qr_Image=models.ImageField(upload_to='qrcode',blank=True)
    color=models.CharField(max_length=40, default='black')

    def __str__(self):
        return self.email

    def save(self,*args,**kwargs):
      qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=4
      )  
      qr.add_data('company:'+ self.company + '\n')
      qr.add_data('email:' + self.email + '\n')
      qr.add_data('address:'+  self.address + '\n')
      qr.make(fit=True)
      qrcode_img= qr.make_image(fill_color=self.color)
      buffer=BytesIO()
      qrcode_img.save(buffer,format='PNG')
      self.Qr_Image.save('myqr.png',File(buffer),save=False)
      super().save(*args,**kwargs)


class Text_Message(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    number=models.CharField(max_length=20)
    text=models.TextField(max_length=250)
    Qr_image=models.ImageField(upload_to='qrcode',blank=True)
    color=models.CharField(max_length=40, default='black')

    def __str__(self):
        return self.number

    def save(self,*args,**kwargs):
      qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=4
      )  
      qr.add_data('Phone Number:'+ self.number + '\n')
      qr.add_data('Text:' + self.text + '\n')
      qr.make(fit=True)
      qrcode_img= qr.make_image(fill_color=self.color)
      buffer=BytesIO()
      qrcode_img.save(buffer,format='PNG')
      self.Qr_image.save('myqr.png',File(buffer),save=False)
      super().save(*args,**kwargs)




class Contact_Details(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    contact_name=models.CharField(max_length=50)
    company=models.CharField(max_length=100)
    website=models.URLField()
    email=models.EmailField()
    number=models.CharField(max_length=15)
    address=models.CharField(max_length=100)
    qr_Image=models.ImageField(upload_to='qrcode',blank=True)
    color=models.CharField(max_length=40, default='black')

    def __str__(self):
        return self.contact_name

    def save(self,*args,**kwargs):
      qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=6,
        border=4
      )  
      qr.add_data('Name:'+ self.contact_name + '\n')
      qr.add_data('Company:'+ self.company + '\n')
      qr.add_data('Website:'+ self.website + '\n')
      qr.add_data('Email:' + self.email + '\n')
      qr.add_data('Number:'+ self.number + '\n')
      qr.add_data('Address:'+  self.address + '\n')
      qr.make(fit=True)
      qrcode_img= qr.make_image(fill_color=self.color)
      buffer=BytesIO()
      qrcode_img.save(buffer,format='PNG')
      self.qr_Image.save('myqr.png',File(buffer),save=False)
      super().save(*args,**kwargs)





