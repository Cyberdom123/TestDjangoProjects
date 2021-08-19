from django.db import models

class User(models.Model):
	username = models.CharField(max_length=32, unique=True)
	phone = models.CharField(max_length=32, unique=True)
	emial = models.EmailField(max_length=254, unique=True)
	password = models.CharField(max_length=256, unique=True)

	def natural_key(self):
		return (self.username)

	def __str__(self):
		return self.username
