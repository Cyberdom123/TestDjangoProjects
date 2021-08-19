from django.shortcuts import render
from .forms import LoginForm, RegisterForm
from .models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(request,
				username=cd['login'],
				password=cd['password'])
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponse('Authenticated '\
									'successfully')
			else:
				return HttpResponse('Disabled account')
		else:
			return HttpResponse('Invalid login')
	else:
		form = LoginForm()
	return render(request, 'login/login.html',{'form':form})

def customlogin(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			login = cd['login']
			password = cd['password']
			try:
				user = User.objects.get(username = login, password = password)
				return HttpResponse('elo')
			except User.DoesNotExist:
				return HttpResponse('nie maaa!')
	else:
		form = LoginForm()
		return render(request, 'login/login.html',{'form':form})

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			phone = request.POST['phone']
			email = request.POST['email']
			password = request.POST['password']

			new_user = User(username=username,phone=phone,
						emial=email, password=password)
			new_user.save()
			return HttpResponse('user saved!')
		else:
			return HttpResponse('not vald form!')
	else:
		form = RegisterForm()
		return render(request, 'register/register.html',{'form':form})	