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
    path('create_link/', views.create_link, name='create_link'),
    path('send_mail/', views.send_mail, name='send_mail'),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)