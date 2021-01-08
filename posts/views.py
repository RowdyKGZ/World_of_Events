from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, \
    DetailView, DeleteView, RedirectView

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


class PostLikeRedirect(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(Post, slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user in obj.likes.all():
            obj.likes.remove(user)
        else:
            obj.likes.add(user)
        return url_
