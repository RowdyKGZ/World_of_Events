from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'posts/index.html'
