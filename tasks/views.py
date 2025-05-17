from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from .models import Category, Task
from user_tasks.models import UserTask
from .serializers import CategorySerializer, TaskSerializer
from django.shortcuts import get_object_or_404


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        difficulty = self.request.query_params.get('difficulty')
        queryset = Task.objects.filter(category_id=category_id)
        if difficulty:
            queryset = queryset.filter(difficulty=difficulty)
        return queryset


class TaskDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


class CheckAnswerView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        task_id = request.data.get('task_id')
        user_answer = request.data.get('user_answer')

        if not task_id or user_answer is None:
            return Response({'error': 'Task ID and user answer are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            task = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        is_correct = (str(user_answer).lower() == str(
            task.correct_answer).lower())

        UserTask.objects.create(
            user=request.user,
            task=task,
            answer=user_answer,
            is_correct=is_correct,
            answer_options=task.answer_options
        )

        if is_correct:
            return Response({'message': 'Correct answer'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong answer'}, status=status.HTTP_200_OK)


class TaskResultView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_tasks = UserTask.objects.filter(user=request.user)
        total_tasks = user_tasks.count()
        correct_answers = user_tasks.filter(is_correct=True).count()
        incorrect_answers = total_tasks - correct_answers
        skipped_tasks = user_tasks.filter(skipped=True).count()

        completed_tasks = total_tasks - skipped_tasks

        total_points = correct_answers
        result = {
            'total_points': total_points,
            'completed_tasks': completed_tasks,
            'skipped_tasks': skipped_tasks,
            'correct_answers': correct_answers,
            'incorrect_answers': incorrect_answers,
        }
        return Response(result, status=status.HTTP_200_OK)
