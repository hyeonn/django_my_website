from django.shortcuts import render, get_object_or_404, redirect
from  . models import Board
from  . models import Post
from django.views.generic import ListView
from django.http import HttpResponse

from  .forms import BoardForm,PostForm

class PostList(ListView):
    model = Post

# Create your views here.

def index(request):
    return  render(
        request,
        'myweb/blog.html'
    )

def board(request):
    boards = Board.objects.exclude(name="Portfolio");
    return  render(
        request,
        'myweb/blog.html',
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


def boardFirst(request):
    posts = Post.objects.filter(board_id=1);
    boards = Board.objects.filter(id=1);

    return  render(
        request,
        'myweb/boardFirst.html',
        #{'boardFirst': boards}
        #{'postsFirst': posts}

    )

def newPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponse("Saved OK")
    else:
        form = PostForm()
        return render(
            request,
            'myweb/postform.html',
            {"form": form}
        )