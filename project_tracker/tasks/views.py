import html
from typing import Any
from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from .models import Project,Task
from django.views.generic import ListView
from django.views import View
from django.template.loader import render_to_string

def index(request):
   return render(request,'tasks/index.html')
   

def project_list(request):
    projects = Project.objects.all()

    return render(request,'tasks/projects_list.html',{'project_list':projects})

def project_detail(request,project_id):
    project = get_object_or_404(Project,id=project_id)
    tasks=project.tasks.all()
    response_html=f'<h1>{project.name}</h1><p>{project.description}</p>'
    response_html+='</ul>'
    return HttpResponse(response_html)
def task_detail(request,project_id,task_id):
    project=get_object_or_404(Project, id=project_id)
    task=get_object_or_404(Task, id=task_id,project=project)
    response_html=f'<h1>{task.name}</h1><p>{task.description}</p>'
    return HttpResponse (response_html)



class IndexView(View):
 def get(self,request,*args,**kwards):
    projects_list_url=reverse('tasks:projects_list')
    html = f"<h1>Страница приложения tasks</h1><a href='{'another_page_url'}'>Перейти на другую страницу</a>" 
    return HttpResponse(html)

class ProjectDetailView (DetailView):
    model=Project
    pk_url_kward ='project_id'

    def get(self, request, *args, **kwargs):
        projects=self.get_queryset()
        projects_html='<h1>Список проектов</h1><ul>'
        for project in projects:
         projects_html=f"<li><a href='{project.id}/'>{project.name}/a></li>"
        projects_html+='</ul>' 
        return HttpResponse(projects_html) 