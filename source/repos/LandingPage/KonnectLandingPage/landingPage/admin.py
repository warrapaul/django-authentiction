from django.contrib import admin
from .models import *

from  django.contrib.auth.models  import  Group  # new


admin.site.unregister(Group)  # new

admin.site.site_header = 'SASAKONNECT'


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['message_subject', 'client_name', 'client_phone', 'message_date_sent']
admin.site.register(ContactUs, ContactUsAdmin)