from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('scheduleservice/form/',views.Service_forms, name="scheduleservice"),
    # path('scheduleservice/done/',views.Scheduler_create.as_view(),name="form"),
]
