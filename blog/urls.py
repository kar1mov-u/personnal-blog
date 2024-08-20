from django.urls import path

from . import views
urlpatterns = [
    path('',views.starting_point,name= 'starting-point-page'),
    path('posts-page',views.posts,name='posts-page'),
    path('posts/<slug>',views.post_detail,name = 'post-detail-page')
]