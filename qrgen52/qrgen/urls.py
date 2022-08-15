from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home, name='home'),
    path('register/',views.register, name='register'),
    path('login/',views.loginpage, name='login'),
    path('about/', views.aboutpage, name='about'),
    path('contact/', views.contactpage, name='contact'),
    path('faq/', views.faqpage, name='faq'),
    path('help/', views.helppage, name='help'),
     path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    
    #qr_pages
    path('create_link/', views.create_link, name='create_link'),
    path('send_mail/', views.send_mail, name='send_mail'),
    path('contact_details/', views.contact_details, name='contact_details'),
    path('text_message/', views.text_message, name='text_message'),
    path('image_upload/', views.image_upload, name='image_upload'),
    path('video/', views.video, name='video'),
    path('audio/', views.audio, name='audio'),
    path('download_link/', views.download_createlink, name='download_link'),
    path('download_contact/', views.download_contact, name='download_contact'),
    path('download_mail/', views.download_mail, name='download_mail'),
    path('download_text/', views.download_text_message, name='download_text'),
    path('<int:pk>/jpeg/', views.download_link_jpeg, name='download_link_jpeg'),
    path('<int:pk>/png/', views.download_link_png, name='download_link_png'),
    path('<int:pk>/pdf/', views.download_link_pdf, name='download_link_pdf'),
    path('<int:pk>/mail_jpeg/', views.download_mail_jpeg, name='download_mail_jpeg'),
    path('<int:pk>/mail_png/', views.download_mail_png, name='download_mail_png'),
    path('<int:pk>/mail_pdf/', views.download_mail_pdf, name='download_mail_pdf'),
    path('<int:pk>/msg_jpeg/', views.download_message_jpeg, name='download_message_jpeg'),
    path('<int:pk>/msg_png/', views.download_message_png, name='download_message_png'),
    path('<int:pk>/msg_pdf/', views.download_message_pdf, name='download_message_pdf'),
    path('<int:pk>/contact_jpeg/', views.download_contact_jpeg, name='download_contact_jpeg'),
    path('<int:pk>contact_/png/', views.download_contact_png, name='download_contact_png'),
    path('<int:pk>/contact_pdf/', views.download_contact_pdf, name='download_contact_pdf'),
    

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)