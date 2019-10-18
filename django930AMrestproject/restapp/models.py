from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Register_User(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	mobile = models.CharField(max_length=10)
	address = models.TextField()
	aadhar_no = models.CharField(max_length=12)

	def __str__(self):
		return self.user.username