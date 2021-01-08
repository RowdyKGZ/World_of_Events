from django import forms
from django.core.exceptions import ValidationError

from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image']

        widget = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ImageField(),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        return new_slug
