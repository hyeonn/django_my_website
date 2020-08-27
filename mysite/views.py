from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.http import HttpResponse
from myweb.models import Project


# Create your views here.
class PortfolioProject(ListView):
    model = Project

    def get_queryset(self):
        return Project.objects.order_by('-id')

def main(request):
    return  render(
        request,
        'startbootstrap/main.html'
    )

'''def portfolio(request):
    posts = Post.objects.filter(Board_id=4)
    return  render(
        request,
        'project_list.html',
        {
            'posts': posts
        }
    )
'''
