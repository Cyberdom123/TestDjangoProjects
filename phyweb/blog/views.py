from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage,\
PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from .forms import EmailPostForm, CommentForm

def post_list(request):  #fonctoion based view, now its out of use
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) #3 post on each page
    page = request.GET.get('page')

    try:
    	posts = paginator.page(page)
    except PageNotAnInteger:
    	#if page is not an intrger deliver the first page
    	posts = paginator.page(1)
    except EmptyPage:
    	#if page is out of range deliver the last page of results
    	posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'page': page,
    											 'posts': posts})
class PostListView(ListView): #same view based on class, site view with object list.
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, 
        slug = post, 
        status = 'published',   #str 27 
        publish__year = year,
        publish__month = month,
        publish__day = day)
    #list of active commens for this post
    comments = post.comment.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        # create comment object but don't save to database yet
        new_comment = comment_form.save()
        # Assign the current post to the comment
        new_comment.post = post
        #Save the commnet
        new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post/detail.html', {'post': post,
                                                    'comment':comment,
                                                    'new_comment':new_comment,
                                                    'comment_form':comment_form})

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

# Create your views here.