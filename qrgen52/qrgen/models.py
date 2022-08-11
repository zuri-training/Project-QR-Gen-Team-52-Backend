from asyncio import constants
from django.db import models
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
from django.contrib.auth.models import User

# Create your models here.
import random
class Create_link(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    url=models.URLField()
    image=models.ImageField(upload_to='qrcode',blank=True)
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
      canvas=Image.new("RGB", (300,300),"white")
      draw=ImageDraw.Draw(canvas)
      canvas.paste(qrcode_img)
      buffer=BytesIO()
      canvas.save(buffer,"PNG")
      self.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
      canvas.close()
      super().save(*args,**kwargs)


class Send_Mail(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    company=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.CharField(max_length=100)
    image=models.ImageField(upload_to='qrcode',blank=True)
    color=models.CharField(max_length=40, default='black')

    def __str__(self):
        return self.email

    def save(self,*args,**kwargs):
      qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=4
      )  
      qr.add_data('company:'+ self.company + '\n')
      qr.add_data('email:' + self.email + '\n')
      qr.add_data('address:'+  self.address + '\n')
      qr.make(fit=True)
      qrcode_img= qr.make_image(fill_color='blue')
      canvas=Image.new("RGB", (300,300),"white")
      draw=ImageDraw.Draw(canvas)
      canvas.paste(qrcode_img)
      buffer=BytesIO()
      canvas.save(buffer,"PNG")
      self.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
      canvas.close()
      super().save(*args,**kwargs)

