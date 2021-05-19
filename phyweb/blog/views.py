from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage,\
PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from .forms import EmailPostForm, CommentForm


class PostListView(ListView):  #same view based on class, site view with object list.
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'blog/post/list.html'

def post_detail(request, year, month, day, post):

    post = get_object_or_404(Post,
        slug = post, 
        status = 'published',   #str 27 
        publish__year = year,
        publish__month = month,
        publish__day = day)
    #list of active commens for this post
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # from fields passed validation
            cd = form.cleaned_data
            #send email
            post_url = request.build_absolute_uri(
                    post.get_absolute_url())
            subject = f"{cd['name']} recommends you read " \
                    f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                    f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'admin@myblog.com',
                    [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    return render(request, 'blog/post/detail.html', {'post': post,
                                                    'form': form})

def post_share(request, post_id):
    # Retrive post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # from fields passed validation
            cd = form.cleaned_data
            #send email
            post_url = request.build_absolute_uri(
                    post.get_absolute_url())
            subject = f"{cd['name']} recommends you read " \
                    f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                    f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'admin@myblog.com',
                    [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post':post, 
                                                    'form':form,
                                                    'sent':sent})

def TestPage(request):

    form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'form':form})
# Create your views here.