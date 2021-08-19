from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	login = forms.CharField(min_length=7, max_length=254,
							widget=forms.TextInput(attrs={'placeholder': 'Login'}), 
							required = True,
							label ='')
	password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}),
							required = True,
							label = '')
class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}), 
							required = True,
							label ='', min_length=5, max_length=20)
	phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone'}), 
							required = True,
							label ='')
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), 
							required = True,
							label ='')
	password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}),
							min_length=8, max_length=128, required = True,
							label = '')
	confirm_password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Confirm password'}),
							required = True,
							label = '')

class Login(forms.Form):
	login = forms.CharField(min_length=7, max_length=254,
							widget=forms.TextInput(attrs={'placeholder': 'Login'}), 
							required = True,
							label ='')
	password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}),
							required = True,
							label = '')
	class Meta:
		model = User
		fields = ('username')


class Register(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}), 
							required = True,
							label ='', min_length=5, max_length=20)
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), 
							required = True,
							label ='')
	password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}),
							min_length=8, max_length=128, required = True,
							label = '')
	confirm_password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Confirm password'}),
							required = True,
							label = '')

	class Meta:
		model = User
		fields = ('username', 'email')

	def clean_confirmed_password(self):
		cd = self.cleaned_data
		if cd['password'] != cd['confirm_password']:
			raise forms.ValidationError('Passwords don\'t match.')
		return cd['confirm_password']