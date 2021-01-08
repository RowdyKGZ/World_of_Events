from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from posts.models import Post
from posts.utils import ObjectDetailMixin


class PostListView(ListView):
    """Все посты"""
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'posts/posts_list_view.html'


class PostDetailView(DetailView):
    """Детали постов"""
    model = Post
    template_name = 'posts/post_detail_view.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/post_create_form.html'
    context_object_name = 'post'
    fields = ['title', 'author', 'body', 'slug', 'author', 'image']


class PostUpdateView(UpdateView): # Новый класс
    model = Post
    template_name = 'post_edit_form.html'
    fields = ['title', 'author', 'body', 'slug', 'author', 'image']