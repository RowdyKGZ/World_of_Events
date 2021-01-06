from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

USER = get_user_model()


class Comment(models.Model):
    pass


class Post(models.Model):
    """Модель постов"""
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField(max_length=100, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='related_post')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_pub = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True, null=True)
    like = models.PositiveIntegerField(default=0)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    """Модель хэш-тегов"""
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']