from django.urls import path
from django.contrib.auth import views

from .views import RegisterView, ActivationView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('activate/<uuid:activation_code>/', ActivationView.as_view(), name='activation'),
]
