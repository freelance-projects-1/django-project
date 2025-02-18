from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('projects/', views.project),
    # path('tasks/<str:name>', views.tasks)
    path('tasks/', views.tasks),
    path('create_task/', views.create_task),
    path('create_project/', views.create_project)
]