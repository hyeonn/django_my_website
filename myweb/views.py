from django.shortcuts import render, get_object_or_404, redirect
from  . models import Board
from  . models import Post
from django.views.generic import ListView,CreateView,DetailView
from django.http import HttpResponse


from  .forms import BoardForm,PostForm

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
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


class postlist(ListView):
    #boards = Board.objects.filter(id=1);

    model = Post

    def get_queryset(self):
        return (Post.objects.filter(Board_id=pk).order_by('-id'))

    #render(request, 'myweb/post_list.html', {'boards': boards}),

def newPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #Post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(
            request,
            'myweb/post_form.html',
            {"form": form}
        )


'''
class PostCreate(CreateView):
    model = Post
    fields = [
        'Board_id', 'title' , 'content', 'note'
    ]


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


class PostCreate(CreateView):
    model = Post
    fields = [
        'Board_id', 'title' , 'content', 'note'
    ]
'''