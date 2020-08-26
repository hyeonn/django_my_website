from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.http import HttpResponse
from myweb.models import Post


# Create your views here.
class PortfolioPost(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(Board_id=4).order_by('-id')

def main(request):
    return  render(
        request,
        'startbootstrap/main.html'
    )

'''def portfolio(request):
    posts = Post.objects.filter(Board_id=4)
    return  render(
        request,
        'post_list.html',
        {
            'posts': posts
        }
    )
'''
