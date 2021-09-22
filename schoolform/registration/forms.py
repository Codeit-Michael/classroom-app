from django.forms import ModelForm

# needed for sign ups
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import applicant

class applicantForm(ModelForm):
	class Meta:
		model = applicant
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']