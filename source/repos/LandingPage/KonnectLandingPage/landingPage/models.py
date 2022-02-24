from django.db import models





# Create your models here.

class ContactUs(models.Model):
    client_name = models.CharField(max_length=300, null=True, blank=True)
    client_phone = models.CharField(max_length=20, null=True, blank=True)
    client_email = models.EmailField()
    message_subject = models.CharField(max_length=75)
    message = models.TextField()
    message_date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.message_subject) + '_' + str(self.client_email)

