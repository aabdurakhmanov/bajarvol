from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        task = self.get_object()
        if task.status == 'completed':
            return Response({'detail': 'Allaqachon bajarilgan'}, status=400)

        task.status = 'completed'
        task.completed_at = timezone.now()
        task.save()

        user = request.user
        user.coins += 10
        user.stars += 1
        user.save()

        return Response({'detail': 'Vazifa bajarildi, mukofot berildi!'})
