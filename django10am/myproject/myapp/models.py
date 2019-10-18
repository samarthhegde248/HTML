from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Register(models.Model):
	name=models.CharField(max_length=25)
	email=models.CharField(max_length=25)
	mobile=models.CharField(max_length=10)

	def __str__(self):
		return self.name

class Custom_User(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	mobile = models.CharField(max_length=10)
	address = models.TextField()
	aadhar_no = models.CharField(max_length=12)
	profile_pic = models.FileField(upload_to='userimages')

	def __str__(self):
		return self.user.username