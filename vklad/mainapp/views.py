from django.shortcuts import render
from datetime import datetime
import locale

# Create your views here.
def index(request):
    locale.setlocale(locale.LC_TIME, 'ru_RU')

    today = datetime.now().date()
    context = {
        'today': today
    }

    return render(request, 'home-tech-blog.html', context=context)