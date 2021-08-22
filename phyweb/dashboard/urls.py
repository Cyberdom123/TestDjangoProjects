from django.urls import path
from  . import views

app_name = 'dashboard'
urlpatterns = [
	path('bar/', views.bar, name='bar')
]