from django import forms

# needed for sign ups
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import applicant

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']