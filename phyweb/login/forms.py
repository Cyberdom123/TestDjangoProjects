from django import forms

class LoginForm(forms.Form):
	login = forms.CharField(min_length=7, max_length=254,
							widget=forms.TextInput(attrs={'placeholder': 'Email or phone'}), 
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