from django.db import models

class User(models.Model):
	username = models.CharField(max_length=32)
	phone = models.CharField(max_length=32)
	emial = models.EmailField(max_length=254)
	password = models.CharField(max_length=256)

	def natural_key(self):
		return (self.username)