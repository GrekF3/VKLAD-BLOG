from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Category
from django.views.generic import ListView


class BlogPostListView(ListView):
    model = BlogPost
    template_name = "post-list.html"

def post_detail(request, category_slug, post_slug):
    category = get_object_or_404(Category, slug=category_slug)
    post = get_object_or_404(BlogPost, slug=post_slug, category=category)
    # Дополнительная логика и контекст для отображения поста
    return render(request, 'post-layout-2.html', {'post': post})