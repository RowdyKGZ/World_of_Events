from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View

from .models import Post


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})
