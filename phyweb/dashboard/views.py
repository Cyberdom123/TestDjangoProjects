from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.views.generic import ListView
from blog.forms import EmailPostForm, CommentForm


@login_required
def user_dashboard(request):

# Create your views here.	