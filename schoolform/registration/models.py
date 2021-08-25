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
	firstname = models.CharField(max_length=15)
	lastname = models.CharField(max_length=15)
	gender = models.CharField(max_length=10,choices=GENDER_CHOICE)
	phone = models.IntegerField()
	guardian = models.CharField(max_length=25)
	guardians_phone = models.IntegerField()
	address = models.CharField(max_length=60)
	course = models.CharField(max_length=30,choices=COURSE_CHOICE)