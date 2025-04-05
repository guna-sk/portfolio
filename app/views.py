from django.shortcuts import render,redirect
from django.http import HttpResponse,FileResponse
from django.core.mail import send_mail
from app.forms import *
import os
from django.conf import settings
# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def project(request):
    return render(request, 'project.html')

def skills(request):
    return render(request, 'skills.html')

from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            user_email = form.cleaned_data['email']
            full_message = f"From: {user_email}\n\n{message}"
            email = EmailMessage(
                subject=subject,
                body=full_message,
                from_email="your-email@gmail.com",  
                to=['asguna1511@gmail.com'],
                reply_to=[user_email], 
            )
            email.send() 
            return redirect('success')
    else: 
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def success(request):
    return render(request,'success.html')

def download(request):
    file_path=os.path.join(settings.MEDIA_ROOT,'Cv.pdf')
    return FileResponse(open(file_path,'rb'),as_attachment=True,content_type='application/pdf')