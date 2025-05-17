from rest_framework import serializers
from .models import UserTask
from tasks.models import Task

class UserTaskSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all())
    class Meta:
        model = UserTask
        fields = ('id', 'user', 'task', 'answer', 'is_correct', 'skipped', 'answered_at', 'answer_options')
        read_only_fields = ('is_correct', 'skipped', 'answered_at', 'answer_options', 'user')