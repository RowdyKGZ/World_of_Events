from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list_view'),
    path('create/', PostCreateView.as_view(), name='post_create_url'),
    path('<str:slug>/', PostDetailView.as_view(), name='post_detail_view'),
    path('<int:id/edit/', PostUpdateView.as_view(), name='post_edit_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)