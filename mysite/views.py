from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.http import HttpResponse
from myweb.models import Project,ProjectComment,VisitorsBook
from myweb.forms import ProjectCommentForm,VisitorsBookForm


# Create your views here.
class PortfolioProject(ListView):
    model = Project

    def get_queryset(self):
        return Project.objects.order_by('-id')

# class VisitorsBooks(ListView):
#     model = VisitorsBook
#
#     def get_queryset(self):
#         return VisitorsBook.objects.order_by('-id')

def VisitorsBooks(request):
    visitorsBooks = VisitorsBook.objects.all().order_by('-id')
    if request.method == "POST":
        visitorsBook_form = VisitorsBookForm(request.POST)
        if visitorsBook_form.is_valid():
            visitorsBook = visitorsBook_form.save(commit=False)
            visitorsBook.save()
            return redirect('VisitorsBooks')
    else:
        visitorsBook_form = VisitorsBookForm()
        visitorsBooks = VisitorsBook.objects.all().order_by('-id')
    return render(
        request,
        'myweb/visitorsbook_list.html',
        {'visitorsBook_form':visitorsBook_form,'visitorsBooks': visitorsBooks}

    )

def main(request):
    return  render(
        request,
        'startbootstrap/main.html'
    )
def ProjectDetail(request,pk):
    project = get_object_or_404(Project, pk=pk)
    Project.objects.filter(pk=pk).update(views=Project.objects.get(pk=pk).views + 1)
    if request.method == "POST":
        pcomment_form = ProjectCommentForm(request.POST)
        if pcomment_form.is_valid():
            pcomment = pcomment_form.save(commit=False)
            pcomment.Project = project
            pcomment.save()
            return redirect('project_detail', pk=project.pk)
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
