from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from .views import PostDetailView, PostCreateView, PostUpdateView, \
    PostDeleteView, PostLikeRedirect, CommentCreateView, CommentUpdateView, \
    CommentDeleteView, posts_list, tags_list, TagCreateView, TagUpdateView, \
    tags_list, TagDetailView, TagDeleteView


urlpatterns = [
    path('', posts_list, name='post_list_view'),
    path('create/', PostCreateView.as_view(), name='post_create_url'),
    path('<str:slug>/', PostDetailView.as_view(), name='post_detail_view'),
    path('<str:slug>/like/', PostLikeRedirect.as_view(), name='post_like'),
    path('<str:slug>/update/', PostUpdateView.as_view(), name='post_update_url'),
    path('<str:slug>/delete/', PostDeleteView.as_view(), name='post_delete_url'),
    path('comment/create/', CommentCreateView.as_view(), name='comment_create_url'),
    path('comment_update/<str:slug>/', CommentUpdateView.as_view(), name='comment_update_url'),
    path('comment_delete/<str:slug>/', CommentDeleteView.as_view(), name='comment_delete_url'),
    path('tag/list/', tags_list, name='tags_list_view'),
    path('tag/create/', TagCreateView.as_view(), name='tag_create_view'),
    path('tag/<str:slug>/update/', TagUpdateView.as_view(), name='tag_update_view'),
    path('tag/<str:slug>/detail', TagDetailView.as_view(), name='tag_detail_view'),
    path('tag/<str:slug>/delete', TagDeleteView.as_view(), name='tag_delete_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
