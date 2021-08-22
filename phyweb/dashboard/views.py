from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from blog.forms import EmailPostForm, CommentForm


def bar(request):
	return render(request, 'dashboard/bar.html')