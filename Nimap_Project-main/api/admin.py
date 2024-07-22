# api/admin.py

from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'client', 'created_by', 'created_at', 'updated_at']
    search_fields = ['name', 'client__name', 'created_by__username']
    list_filter = ['client', 'created_by']

admin.site.register(Project, ProjectAdmin)
