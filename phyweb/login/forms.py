from django import forms

class LoginForm(forms.Form):
	login = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email or phone'}), 
							required = True,
							label ='')
	password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}),
							required = True,
							label = '')
