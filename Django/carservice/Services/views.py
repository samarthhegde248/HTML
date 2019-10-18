from django.shortcuts import render
from django.http import HttpResponse
from .forms import Service_Form
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import SchedulerDetails, CarServiceDetail
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .serializers import DetailsSerializer
from django.core.mail import send_mail
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'freelance.html')

def sendmail(service_date, recpemail):
    subject = 'Appointment for the car service'
    message = 'Your appointment successfull on the {}.'.format(service_date)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [recpemail]
    send_mail( subject, message, email_from, recipient_list )

def Service_forms(request):
    form = Service_Form()
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        address = request.POST['address']
        city = request.POST['city']
        postal = request.POST['postal']
        country = request.POST['country']
        car_make = request.POST['car_make']
        car_model = request.POST['car_model']
        color = request.POST['color']
        year = request.POST['year']
        service_type = request.POST['service_type']
        service_date = request.POST['service_date']
        if form.is_valid:
            schDet = SchedulerDetails.objects.create(fname = fname, lname = lname, email = email, phone = phone,dob = dob,address = address,city = city,postal = postal,country = country)
            carDet = CarServiceDetail.objects.create(email = schDet, car_make = car_make,car_model = car_model,color = color,year = year,service_type = service_type, service_date = service_date )
            sendmail(service_date, email)
            return HttpResponse("<h1>Your appoinment has been successfull on the date {}, Thank You!</h1>".format(service_date))
        else:
            return HttpResponse("<h1>Unable to Get the appointment for you please TRY AGAIN!</h1>")

    return render(request, 'freelance_services.html', {'form':form})

# class Scheduler_create(CreateView):
#     model= SchedulerDetails
#     fields="__all__"
#     success_url = reverse_lazy('form')
#     template_name = "freelance_services.html"

# class Scheduler_list(ListView):
# 	model=SchedulerDetails

# class Scheduler_detail(DetailView):
# 	model=SchedulerDetails

# class Service_create(CreateView):
#     model = CarServiceDetail
#     fields = "__all__"
#     success_url = reverse_lazy('forms')

# class Service_list(ListView):
# 	model=SchedulerDetails

# class Service_detail(DetailView):
# 	model=SchedulerDetails

# class DetailsView(APIView):
#     def get(self, request):
#         scheduler_details = SchedulerDetails.objects.all()
#         carservice_detail = CarServiceDetail.objects.all()
#         # detail_serializer = DetailSerializer(scheduler_details, many=True)
#         return Response(request, 'waste.html', {"detail_serializer": detail_serializer.data})