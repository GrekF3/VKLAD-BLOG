from django.shortcuts import render
from .models import BlogPost
from django.views.generic import ListView


class BlogPostListView(ListView):
    model = BlogPost
    template_name = "post-list.html"