# tasks/permissions.py
from rest_framework.permissions import BasePermission

class IsAssignedToYou(BasePermission):
    def has_object_permission(self, request, view, obj):
        return getattr(obj, "assigned_to_id", None) == request.user.id
