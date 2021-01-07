from django.urls import path, include

from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list_view'),
    path('<str:slug>/', PostDetailView.as_view(), name='post_detail_view'),
]
