
from django.db import models
from django.contrib.auth import get_user_model
import secrets

User = get_user_model()

class Task(models.Model):
    STATUS_CHOICES = [
        ("TODO", "To Do"),
        ("IN_PROGRESS", "In Progress"),
        ("DONE", "Done"),
    ]
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="TODO")
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} ({self.status})"

class Token(models.Model):
    """
    Minimal token model: one token per user (unique).
    """
    key = models.CharField(max_length=40, unique=True, db_index=True)
    user = models.OneToOneField(User, related_name="api_token", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def generate():
        # 20 bytes -> 40 hex chars, similar to DRF authtoken format
        return secrets.token_hex(20)

    @classmethod
    def get_or_create_for_user(cls, user):
        try:
            return user.api_token
        except cls.DoesNotExist:
            return cls.objects.create(user=user, key=cls.generate())

    def __str__(self):
        return f"{self.user.username}:{self.key[:6]}…"
