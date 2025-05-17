from rest_framework import serializers
from .models import Task, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'category', 'difficulty', 'topic', 'question_number', 'question', 'answer_options', 'correct_answer')
