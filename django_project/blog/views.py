from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render (request, 'blog/home.html', context)

def about(request) :
    return render (request, 'blog/about.html', {'title': 'About'})
##we need url pattern! ets creat urls.py and map the url for each view functionl