from rest_framework import viewsets, permissions
from django.utils import timezone
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwnerOrReadOnly

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.save()
        # Agar status 'completed' bo‘lsa va hali completed_at yozilmagan bo‘lsa
        if instance.status == 'completed' and instance.completed_at is None:
            instance.completed_at = timezone.now()
            instance.save()
