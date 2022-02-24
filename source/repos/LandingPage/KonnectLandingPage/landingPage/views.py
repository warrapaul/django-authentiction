from .models import *
from .forms import ContactUsForm
from django.contrib import messages

from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect


def Home(request):
   if request.method == 'POST':
        contactUSForm = ContactUsForm(request.POST)
        if contactUSForm.is_valid():
            contactUSForm.save()
            contactusfeedback='success'
            messages.success(request, 'Message sent successfully.')
            context = {
            'contactusfeedback': ' success',
            }
            return render(request, 'landingPage/index.html', context)

   elif request.method == "GET":
        contactUSForm = ContactUsForm
        context = {
            'contactUSForm': contactUSForm,
        }
        return render(request, 'landingPage/index.html', context)


