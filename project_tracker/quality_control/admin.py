from django.contrib import admin
from .models import BugReport, FeatureRequest


class BugReportInline(admin.TabularInline):
    model=BugReport
    extra = 0
    fields = ('title','description','project','status', 'task', 'created_at')
    readonly_fields = ('created_at','updated_at')
    can_delete = True
    show_change_link = True
    
@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'project', 'task', 'priority', 'created_at')
    list_filter = ('status', 'project', 'task')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'project', 'task', 'status', 'priority')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    actions = ['mark_as_completed']

    def mark_as_completed(self, request, queryset):
        queryset.update(status='Completed')


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'project', 'task', 'priority', 'created_at')
    list_filter = ('status', 'project', 'task')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'project', 'task', 'status', 'priority')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

