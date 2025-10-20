# tasks/schema.py
import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth.decorators import login_required
from .models import Task

class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = ("id", "title", "status", "created_at", "assigned_to")

class Query(graphene.ObjectType):
    my_tasks = graphene.List(TaskType)

    @login_required
    def resolve_my_tasks(self, info, **kwargs):
        user = info.context.user
        return Task.objects.filter(assigned_to=user).order_by("-created_at")

schema = graphene.Schema(query=Query)
