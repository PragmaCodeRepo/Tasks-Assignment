# tasks/views.py
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Task, Token
from .serializers import TaskSerializer
from .permissions import IsAssignedToYou

class ObtainTokenView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        from django.contrib.auth import authenticate
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"detail": "Invalid credentials"}, status=400)
        token = Token.get_or_create_for_user(user)
        return Response({"token": token.key})

class MyTaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsAssignedToYou]

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)

    def get_object(self):
        obj = get_object_or_404(Task, pk=self.kwargs["pk"], assigned_to=self.request.user)
        self.check_object_permissions(self.request, obj)
        return obj
