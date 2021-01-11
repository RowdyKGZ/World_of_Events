from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, \
    DetailView, DeleteView, RedirectView
from django.core.paginator import Paginator
from .models import Post, Comment, Tag


def posts_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    return render(request, 'posts/posts_list_view.html', context={'posts': page})


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
    fields = ['title', 'author', 'body', 'slug', 'author', 'image', 'tags']


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


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'posts/comment_create_form.html'
    context_object_name = 'post'
    fields = ['post', 'name', 'title',  'body', 'date_added', 'slug']
    success_url = reverse_lazy('post_list_view')


class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'posts/comment_edit_form.html'
    fields = ['name', 'title', 'body', 'slug']
    success_url = reverse_lazy('post_list_view')


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'posts/comment_delete_form.html'
    success_url = reverse_lazy('post_list_view')


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'posts/tags_list_view.html', context={'tags': tags})


class TagCreateView(CreateView):
    model = Tag
    template_name = 'posts/tag_create_form.html'
    context_object_name = 'tag'
    fields = ['title', 'slug']


class TagUpdateView(UpdateView):
    model = Tag
    template_name = 'posts/tag_update_view.html'
    fields = ['title', 'slug']
    success_url = reverse_lazy('tags_list_view')


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'posts/tags_list_view.html', context={'tags': tags})


class TagDetailView(DetailView):
    """Детали тэгов"""
    model = Tag
    template_name = 'posts/tag_detail_view.html'
    context_object_name = 'tag'


class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'posts/tag_delete_form.html'
    success_url = reverse_lazy('tags_list_view')
