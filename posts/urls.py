from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, \
    PostDeleteView


urlpatterns = [
    path('', PostListView.as_view(), name='post_list_view'),
    path('create/', PostCreateView.as_view(), name='post_create_url'),
    path('<str:slug>/', PostDetailView.as_view(), name='post_detail_view'),
    path('<str:slug>/edit/', PostUpdateView.as_view(), name='post_update_url'),
    path('<str:slug>/delete/', PostDeleteView.as_view(), name='post_delete_url'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
