from django.db import models

# Create your models here.
class student(models.Model):
	firstname = models.CharField(max_length=20, blank=True, default='')
	lastname = models.CharField(max_length=20, blank=True, default='')
	age = models.IntegerField(blank=True)

	def __str__(self):
		return self.firstname