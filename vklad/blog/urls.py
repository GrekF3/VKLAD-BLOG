from django.urls import path
from .views import BlogPostListView, post_detail

urlpatterns = [
    path('blog/', BlogPostListView.as_view(), name='Посты'),
    path('<str:category_slug>/<str:post_slug>/', post_detail, name='post_detail'),
]
