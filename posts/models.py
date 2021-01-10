from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField

USER = get_user_model()


class Post(models.Model):
    """Модель постов"""
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    body = RichTextField(blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='related_post')
    author = models.ForeignKey(USER, on_delete=models.CASCADE)
    date_pub = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True, null=True)
    likes = models.ManyToManyField(USER, related_name='blogpost_like', default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail_view', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    def get_like_url(self):
        return reverse('post_like', kwargs={'slug': self.slug})


class Tag(models.Model):
    """Модель хэш-тегов"""
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', default=Post)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    body = RichTextField(blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name} {self.title}'

    def get_absolute_url(self):
        return reverse('post_detail_view', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('comment_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('comment_delete_url', kwargs={'slug': self.slug})
