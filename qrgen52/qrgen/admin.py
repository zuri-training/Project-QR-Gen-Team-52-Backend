from django.contrib import admin
from .models import Create_link, Text_Message, Contact_Details
from .models import Send_Mail


admin.site.register(Create_link)
admin.site.register(Send_Mail)
admin.site.register(Text_Message)
admin.site.register(Contact_Details)
