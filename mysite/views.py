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
def ProjectDetail(request,pk):
    project = get_object_or_404(Project, pk=pk)
    # comment_form = CommentForm(request.POST)
    # comment_form.instance.pk = pk
    # if comment_form.is_valid():
    #     comment = comment_form.save()
    # comment_form = CommentForm()
    # comments = Comment.objects.all()
    return render(request, 'myweb/project_detail.html', {'project': project})
    # { 'comments': comments, 'comment_form': comment_form}

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
