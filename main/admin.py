from django.contrib import admin
from main.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created', 'due_on', 'owner', 'mark']
    list_filter = ['mark']
    search_fields = ['name', 'owner']
    list_editable = ['mark', 'due_on']
    ordering = ['created', 'due_on']
