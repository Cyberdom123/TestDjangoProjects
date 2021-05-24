from django.shortcuts import render
from .forms import LoginForm
from .models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

#def login(request):
#	form = LoginForm()
#	return render(request, 'login/login.html', {'form':form})


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
			username = cd['login']
			password = cd['password']
			try:
				user = User._deflaut_manager.get_by_natural_key(username)
			except User.DoesNotExist:
				return None
