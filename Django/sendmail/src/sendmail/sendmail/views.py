from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def home(request):

    return render(request, 'home.html')

def sendmail(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['insamzone@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )

    return HttpResponse('Mail Successfully sent')