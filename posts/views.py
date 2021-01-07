from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    """Все посты"""
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'posts/posts_list_view.html'


class PostDetailView(DetailView):
    """Детали постов"""
    model = Post
    context_object_name = 'post'
    template_name = "posts/post_detail_view.html"
