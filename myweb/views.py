from django.shortcuts import render, get_object_or_404, redirect
from  . models import Board
from  . models import Post
from django.views.generic import ListView
from django.http import HttpResponse

from  .forms import BoardForm

class PostList(ListView):
    model = Post

# Create your views here.

def index(request):
    return  render(
        request,
        'myweb/main.html'
    )

def board(request):
    boards = Board.objects.all()
    return  render(
        request,
        'myweb/board.html',
        {'boards': boards}

    )

def newBoard(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.save()
            return HttpResponse("Saved OK")
    else:
        form = BoardForm()
        return render(
            request,
            'myweb/boardform.html',
            {"form":form}
        )