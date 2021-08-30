from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

# for manual user sign up form
from django.contrib.auth.forms import UserCreationForm

# for based user sign up form
from .forms import CreateUserForm

# for message
from django.contrib import messages

# for authentication
from django.contrib.auth import authenticate,login,logout

# for login restrictions
from django.contrib.auth.decorators import login_required

# for registration forms
from .forms import applicantForm

# Create your views here.
@login_required(login_url='signin')
def home(request):
	# form = 'hello'
	if request.method == 'POST':
		form = applicantForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('bobo ka')
	else:
		form = applicantForm()
	return render(request,'registration/home.html',{'form':form})


def signUp(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		myForm = CreateUserForm()
		if request.method == 'POST':
			myForm = CreateUserForm(request.POST)
			if myForm.is_valid():
				myForm.save()
				myName = myForm.cleaned_data.get('username') # to get the username only
				messages.success(request,f'user {myName} is successfully created')	# message
				return redirect('login')
		
		return render(request,'registration/signup.html',{'form':myForm})


def signIn(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')	# gets the username from request
			password = request.POST.get('password')	# gets the password from request
			# authentication
			user = authenticate(request,username=username,password=password)

			# log in process
			if user is not None:
				login(request,user)
				return redirect('home')

		return render(request,'registration/signin.html',{})


def signOut(request):
	logout(request)
	return redirect('signin')