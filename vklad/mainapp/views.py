from django.shortcuts import render
from datetime import datetime
import locale
from blog.models import BlogPost, Category

# Create your views here.
def index(request):
    locale.setlocale(locale.LC_TIME, 'ru_RU')
    posts = BlogPost.objects.all()
    categories = Category.objects.all()

    latest_post = BlogPost.objects.order_by('-publication_date').first()

    today = datetime.now().date()

    context = {
        'today': today,
        'posts_list': posts,
        'categories' : categories,
        'latest_post' : latest_post,
    }

    return render(request, 'home-tech-blog.html', context=context)