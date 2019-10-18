from django.db import models

# Create your models here.
class SchedulerDetails(models.Model):
	fname = models.CharField(max_length = 25)
	lname = models.CharField(max_length = 25)
	email = models.EmailField(max_length = 40)
	phone = models.CharField(max_length = 10)
	dob = models.DateField()
	address = models.TextField()
	city = models.CharField(max_length = 15)
	postal = models.IntegerField()
	country = models.CharField(max_length = 15)
	def __str__(self):
		return self.email

class CarServiceDetail(models.Model):
	email = models.ForeignKey(SchedulerDetails, on_delete = models.CASCADE)
	car_make = models.CharField(max_length = 25)
	car_model = models.CharField(max_length = 25)
	color = models.CharField(max_length = 15)
	year = models.CharField(max_length = 4)
	service_type = models.CharField(max_length = 25)
	service_date = models.DateField()
	def __str__(self):
		return self.car_make