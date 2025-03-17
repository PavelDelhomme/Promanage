from django.contrib import admin
from .models import Project, Task, Bug

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'start_date', 'is_public')
    list_filter = ('category', 'status', 'is_public')
    search_fields = ('title', 'description')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'due_date')
    list_filter = ('status', 'project')
    search_fields = ('title', 'description')

@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'priority')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')