from django.urls import path, include

from .views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list_view'),
]