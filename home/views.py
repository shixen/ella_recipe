from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(staus=1)
    template_name = 'index.html'
