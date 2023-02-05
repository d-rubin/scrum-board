from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'author', 'assignees', 'created_at', 'due_date')
    list_display = ('title', 'description', 'author', 'created_at', 'due_date')
    search_fields = ('title', 'author',)


admin.site.register(Todo, TodoAdmin)
