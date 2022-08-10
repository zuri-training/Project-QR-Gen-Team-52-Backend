from django.urls import path
from . import views
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('about/', views.aboutpage, name='about'),
    path('contact/', views.contactpage, name='contact'),
    path('faq/', views.faqpage, name='faq'),

    # qr pages
    path('create-qr/', views.create_qr, name='create-qr'),
    path('audio-qr/', views.audio_qr, name='audio-qr'),
    path('image-qr/', views.image_qr, name='image-qr'),
    path('video-qr/', views.video_qr, name='video-qr'),

    

    path('qr_code/', views.qr_code, name="qr_code"),
]
