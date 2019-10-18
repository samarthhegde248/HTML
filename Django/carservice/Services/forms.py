from django import forms
from .models import SchedulerDetails, CarServiceDetail
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class Service_Form(forms.Form):
    fname = forms.CharField(max_length = 25)
    lname = forms.CharField(max_length = 25)
    email = forms.EmailField(max_length = 40)
    phone = forms.CharField(max_length = 10)
    dob = forms.CharField()
    address = forms.CharField(max_length = 100)
    city = forms.CharField(max_length = 25)
    postal = forms.IntegerField()
    country = forms.CharField(max_length = 20)
    car_make = forms.CharField(max_length = 25)
    car_model = forms.CharField(max_length = 25)
    color = forms.CharField(max_length = 15)
    year = forms.CharField(max_length = 4)
    service_type = forms.CharField(max_length = 25)
    service_date = forms.CharField()