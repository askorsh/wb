from django.urls import path
from . import views
from .views import HomeView, bug_report_list, BugReportDetailView, feature_request_list, FeatureRequestDetailView

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('features/', views.feature_list, name='feature_list'),
    path('bug/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    path('feature/<int:feature_id>/', views.feature_id_detail, name='feature_id_detail'),
    path('', HomeView.as_view(), name='home'),
    path('bug-reports/', bug_report_list, name='bug_report_list'),
    path('bug-reports/<int:pk>/', BugReportDetailView.as_view(), name='bug_report_detail'),
    path('feature-requests/', feature_request_list, name='feature_request_list'),
    path('feature-requests/<int:pk>/', FeatureRequestDetailView.as_view(), name='feature_request_detail'),
]
