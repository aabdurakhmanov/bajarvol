from rest_framework import serializers
from .models import Task
from datetime import datetime

class TaskSerializer(serializers.ModelSerializer):
    # user maydonini faqat o‘qish uchun, username sifatida ko‘rsatamiz
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = [
            'id',
            'user',
            'title',
            'description',
            'status',
            'deadline',
            'completed_at',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['user', 'created_at', 'updated_at', 'completed_at']

    def update(self, instance, validated_data):
        # Agar status completed bo‘lsa va completed_at hali bo‘sh bo‘lsa, vaqtni yozamiz
        if validated_data.get('status') == 'completed' and instance.completed_at is None:
            instance.completed_at = datetime.now()
        return super().update(instance, validated_data)
