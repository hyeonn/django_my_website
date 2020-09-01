from django.shortcuts import render, get_object_or_404, redirect
from  . models import Board
from  . models import Post
from  . models import Comment
from django.views.generic import ListView,CreateView,DetailView
from django.http import HttpResponse
from  .forms import BoardForm,PostForm,CommentForm




def PostDetail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm(request.POST)
    comment_form.instance.pk = pk
    if comment_form.is_valid():
        comment = comment_form.save()
    comment_form = CommentForm()
    comments = Comment.objects.all()
    return render(request, 'myweb/post_detail.html', {'post': post,'comments': comments, 'comment_form': comment_form})


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


'''class postlist(ListView):

    model = Post

    # def get(self, request, pk):
    #     Post_data = Post.objects.filter(Board_id=pk).values()
    def get_queryset(self, boardnum):
        return (Post.objects.filter(Board_id=boardnum).order_by('-id'))

    #render(request, 'myweb/post_list.html', {'boards': boards}),'''

def post_list(request,pk):
    board = Board.objects.filter(id=pk)
    posts = Post.objects.filter(Board_id=pk).order_by('-id')
    return render(request, 'myweb/post_list.html', {'board':board,'posts': posts})




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