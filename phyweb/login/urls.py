from django.urls import path
from  . import views

urlpatterns = [
	path('login/', views.customlogin, name='login'),
	path('register/', views.register, name='register')
]