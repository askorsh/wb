from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from tasks import views
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import BugReport, FeatureRequest
def index(request):
    return HttpResponse("Страница обзора системы контроля качества. <a href='/bugs/'>Список всех багов</a> <a href='/features/'>Запросы на улучшение</a>")

def buglist(request):
    return HttpResponse("Cписок отчетов об ошибках")

def featurelist(request):
    return HttpResponse("Список запросов на улучшение")

def bug_detail(request, bug_id):
    return HttpResponse(f'Детали ошибки: {bug_id}')

def feature_id_detail(request, feature_id):
    return HttpResponse(f'Детали улучшения: {feature_id}')

def tasks_index(request):
    quality_control_home_url = reverse('quality_control:index')
    html = f"<h1>Страница приложения tasks</h1><a href='{quality_control_home_url}'>Перейти на главную страницу приложения quality_control</a>"
    return HttpResponse(html)

def home(request):
    return render(request, 'quality_control/home.html')

class HomeView(ListView):
    template_name = 'quality_control/home.html'
    model = BugReport  

def bug_report_list(request):
    bug_reports = BugReport.objects.all()
    return render(request, 'quality_control/bug_report_list.html', {'bug_reports': bug_reports})

class BugReportDetailView(DetailView):
    template_name = 'quality_control/bug_report_detail.html'
    model = BugReport

def feature_request_list(request):
    feature_requests = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_request_list.html', {'feature_requests': feature_requests})

class FeatureRequestDetailView(DetailView):
    template_name = 'quality_control/feature_request_detail.html'
    model = FeatureRequest
