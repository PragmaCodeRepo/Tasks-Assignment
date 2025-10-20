from django.contrib import admin
from .models import Task, Token

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "assigned_to", "created_at")
    list_filter = ("status", "assigned_to")
    search_fields = ("title",)

@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ("key", "user", "created")
    search_fields = ("key", "user__username")
