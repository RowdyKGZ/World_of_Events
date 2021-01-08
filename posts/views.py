from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, \
    DetailView, DeleteView

from posts.models import Post


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


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post_edit_form.html'
    fields = ['title', 'author', 'body', 'slug', 'author', 'image']


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_delete_form.html'
    success_url = reverse_lazy('post_list_view')
