from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Textarea, Select
from .models import ContactUs
from django.utils.translation import gettext_lazy as _

MESSAGE_SUBJECTS = [('', ''),
                    ('INSTALLATION_REQUEST', ' Installation Request'),
                    ('REPORT_NETWORKS_ISSUE', 'Report Network Issue'),
                    ('COMMENT_COMPLAIN', 'Comment/ Complain')]


class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = ['client_name', 'client_phone', 'client_email', 'message_subject', 'message']
        labels = {
            'client_name': '',
            'client_phone':'',
            'client_email':'',
            'message_subject': '',
            'message': _('Message'),
        }

        widgets = {
            'client_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;'
            }),
            'client_phone': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;'
            }),
            'client_email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;'
            }),
            'message_subject': Select(choices=MESSAGE_SUBJECTS, attrs={
                'class': "form-control dropdown",
                'style': 'max-width: 400px;',
            }),
            'message': Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                 'style': 'height: 150px;',
            })
        }