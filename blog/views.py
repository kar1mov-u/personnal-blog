from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def starting_point(request):
    response = render(request,'blog/starting.html')
    return response
    
def posts(request):
    pass

def post_detail(request):
    pass