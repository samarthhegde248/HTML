from django.db import models

# Create your models here.
class musicLibrary(models.Model):
	songName = models.CharField(max_length = 50)
	artist = models.CharField(max_length = 50)
	genre =models.CharField(max_length = 20)
	def __str__(self):
		return self.songName