from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.http import HttpResponse
from myweb.models import Project,ProjectComment
from myweb.forms import ProjectCommentForm


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
    Project.objects.filter(pk=pk).update(views=Project.objects.get(pk=pk).views + 1)
    if request.method == "POST":
        pcomment_form = ProjectComment(request.POST)
        if pcomment_form.is_valid():
            pcomment = pcomment_form.save(commit=False)
            pcomment.Project = project
            pcomment.save()
            return redirect('post_detail', pk=project.pk)
    else:
        pcomment_form = ProjectCommentForm()
        pcomments = ProjectComment.objects.filter(Project_id=pk)
    return render(request, 'myweb/project_detail.html', {'project': project, 'pcomments': pcomments, 'pcomment_form': pcomment_form})
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
