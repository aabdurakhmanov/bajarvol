from django.contrib import admin
from .models import Task

# Register your models here.

admin.site.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_completed', 'created_at')
    search_fields = ('title',)
    list_filter = ('is_completed', 'created_at')
    ordering = ('-created_at',)
