from django.http import HttpResponse
from .models import Project
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
  title = 'Django!!'
  return render(request, 'index.html', {
    'title': title
  })

def about(request):
  username = 'fazt'
  return render(request, 'about.html', {
    'username': username
  })  

def hello(request, username):
  print(username)
  return HttpResponse("<h2>Hello World %s</h2>" %username)

def project(request):
  # projects = list(Project.objects.values())
  projects = Project.objects.all()
  # return JsonResponse(projects, safe=False)
  return render(request, 'project.html',{
    'projects': projects
  })  

def tasks(request):
  # task=Task.objects.get(title=name)
  # print(name)
  # task=get_object_or_404(Task, id=id)
  # return HttpResponse('task: %s' % task.title)
  return render(request, 'tasks.html')  
