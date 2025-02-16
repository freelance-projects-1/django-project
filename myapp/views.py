from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

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
  return render(request, 'projects/project.html',{
    'projects': projects
  })  

def create_project(request):
  if request.method == 'GET':
    return render(request, 'projects/create_project.html',{
      'form': CreateNewProject()
    })
  else:
      print(request.POST)
      project = Project.objects.create(name=request.POST['name'])
      print(project)
      return redirect('/projects/')

def tasks(request):
  # task=Task.objects.get(title=name)
  # print(name)
  # task=get_object_or_404(Task, id=id)
  # return HttpResponse('task: %s' % task.title)
  tasks = Task.objects.all()
  return render(request, 'tasks/tasks.html', {
    'tasks': tasks
  })  


def create_task(request):
  if request.method == 'GET':
    return render(request, 'tasks/create_task.html', {
      'form': CreateNewTask()
    })
  else:
    Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=1)
    return redirect('/tasks/')
    
