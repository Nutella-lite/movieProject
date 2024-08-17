from django.shortcuts import render, redirect
from datetime import datetime
from .models import Posts
from .forms import PostForm

def index(request):
    reviews = Posts.objects.all()
    data = {
        'active_page': 'index',
        'reviews': reviews
    }
    return render(request, 'films/index.html', data)

def posts(request):
    error = ""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = "Форма заполнена некорректно"
    form = PostForm()
    data = {
        'current_hour': int(datetime.now().strftime('%H')),
        'post_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'active_page': 'posts',
        'form': form,
        'error': error
    }
    return render(request, 'films/posts.html', data)
