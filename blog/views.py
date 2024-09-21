from datetime import date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from .models import Post

# Create your views here.
all_posts =Post.objects.all()

def get_date(post):
    return post['date']

def starting_point(request):
    latest_posts=Post.objects.all().order_by("-date")[:3]
    response = render(request,'blog/index.html',{
        "posts" : latest_posts
    })
    return response
    
def posts(request):
    response = render(request, 'blog/posts.html',{
        "all_posts":all_posts
    })
    return response

def post_detail(request,slug):
    data = get_object_or_404(Post, slug=slug)
    response = render(request,  "blog/single-post.html",{
        "post" : data
    })
    
    return response