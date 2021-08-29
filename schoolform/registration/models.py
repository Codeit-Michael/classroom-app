from django.db import models

GENDER_CHOICE = (
	('M','Male'),
	('F','Female')
)

COURSE_CHOICE = (
	('BSBA','BSBA'),
	('BSIT','BSIT'),
	('BS-EDUC','BS-EDUC'),
	('BS-CRIM','BS-CRIM'),
)

# Create your models here.
class applicant(models.Model):
	username = models.CharField(max_length=50)
	firstname = models.CharField(max_length=15)
	lastname = models.CharField(max_length=15)
	gender = models.CharField(max_length=10,choices=GENDER_CHOICE)
	phone = models.IntegerField()
	email = models.CharField(max_length=70)
	guardian = models.CharField(max_length=25)
	guardians_phone = models.IntegerField()
	address = models.CharField(max_length=200)
	course = models.CharField(max_length=30,choices=COURSE_CHOICE)

	def __str__(self):
		return self.username