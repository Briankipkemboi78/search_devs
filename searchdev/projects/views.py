from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Tag
from .forms import ProjectForm, ReviewForm


def projects(request): 
    projects = Project.objects.all()
    context = { 'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObject = Project.objects.get(id=pk)

    return render(request,'projects/single-project.html' )

def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', " ").split()
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()

            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')


    context = {}
    return render(request, "projects/project_form.html", context)
