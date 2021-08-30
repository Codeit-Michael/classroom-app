from django import forms

# needed for sign ups
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import GENDER_CHOICE,COURSE_CHOICE,applicant

class applicantForm(forms.Form):
	username = forms.CharField(max_length=50)
	firstname = forms.CharField(max_length=15)
	lastname = forms.CharField(max_length=15)
	gender = forms.ChoiceField(choices=GENDER_CHOICE)
	phone = forms.IntegerField()
	email = forms.CharField(max_length=70)
	guardian = forms.CharField(max_length=25)
	guardians_phone = forms.IntegerField()
	address = forms.CharField(max_length=200)
	course = forms.ChoiceField(choices=COURSE_CHOICE)

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']