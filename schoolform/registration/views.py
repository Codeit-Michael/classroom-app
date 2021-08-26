from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# for manual user sign up form
from django.contrib.auth.forms import UserCreationForm

# for based user sign up form
from .forms import CreateUserForm

# Create your views here.
def home(request):
	return HttpResponse('bobo')

def login(request):
	return render(request,'registration/login.html',{})

def signup(request):
	myForm = CreateUserForm()
	if request.method == 'POST':
		myForm = CreateUserForm(request.POST)
		if myForm.is_valid():
			myForm.save()
			return HttpResponseRedirect('/')
	return render(request,'registration/signup.html',{'form':myForm})