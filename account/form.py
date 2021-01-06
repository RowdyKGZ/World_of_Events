from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import MyUser


class UserRegistrationForm(UserCreationForm):
    """Form for create user"""
    class Meta:
        model = MyUser
        fields = ('email', 'password1', 'password2')

    def save(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password1')
        user = get_user_model().object.create_user(email=email, password=password)
        return user



