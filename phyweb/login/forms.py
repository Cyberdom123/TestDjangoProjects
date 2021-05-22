from django import forms

class LoginForm(forms.Form):
	login = forms.CharField(label = "phonenumber, email", 
							required = True)
	password = forms.CharField(label = "Password", max_length = 20,
							required = True)
