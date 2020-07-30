from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage,\
PageNotAnInteger
from django.views.generic import ListView

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

    return render(request, 'blog/post/detail.html', {'post': post})

def post_share(request, post_id):
    # Retrive post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    if request.method == 'POST':
        from = EmailPostForm(request.POST)
        if form.is_valid():
            # from fields passed validation
            cd = form.cleaned_data
            #send email
        else:
            form = EmailPostForm()
        return render(request, 'blog/post/share.html', {'post':post, 
                                                        'form':form})

# Create your views here.