from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import UserTask
from tasks.models import Task
from .serializers import UserTaskSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


User = get_user_model()

class SubmitAnswerView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = UserTaskSerializer(data=request.data)
        if serializer.is_valid():
            task_id = serializer.validated_data['task'].id
            answer = serializer.validated_data['answer']
            task = get_object_or_404(Task, id=task_id)

            is_correct = self.check_answer(task, answer)
            user_task = UserTask.objects.create(
                user=request.user,
                task=task,
                answer=answer,
                is_correct=is_correct,
                answer_options=task.answer_options,
            )
            return Response(
                {"status": "success", "message": "Answer submitted", "data": UserTaskSerializer(user_task).data},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"status": "error", "message": "Invalid data", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def check_answer(self, task, user_answer):
        return str(user_answer).lower() == str(task.correct_answer).lower() # Добавил str() и .lower() для надежного сравнения