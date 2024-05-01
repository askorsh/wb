from django.db import models
from django.contrib.auth.models import User
from tasks.models import Project, Task 

class BugReport(models.Model):
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In progress', 'В работе'),
        ('Completed', 'Завершена')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='bug_reports',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='bug_reports',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )
    priority = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class FeatureRequest(models.Model):
    STATUS_CHOICES = [
        ('Consideration', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='feature_requests',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='feature_requests',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Consideration',
    )
    priority = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
from django.shortcuts import render

def feature_request(request):
    if request.method == 'POST':
        return render(request, 'quality_control/feature_request_success.html')
    return render(request, 'quality_control/feature_request.html')

    def __str__(self):
        return self.title
