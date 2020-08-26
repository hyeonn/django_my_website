from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.http import HttpResponse
from myweb.models import Post


# Create your views here.

def main(request):
    return  render(
        request,
        'startbootstrap/main.html'
    )

def portfolio(request):
    posts = Post.objects.filter(Board_id=4)
    return  render(
        request,
        'portfolio.html',
        {
            'posts': posts
        }
    )

