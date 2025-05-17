from django.db import models
from django.contrib.auth import get_user_model
from tasks.models import Task

User = get_user_model()

class UserTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_tasks')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='user_tasks')
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    skipped = models.BooleanField(default=False)
    answered_at = models.DateTimeField(auto_now_add=True)
    answer_options = models.JSONField(default=list)

    class Meta:
        unique_together = ('user', 'task')

    def __str__(self):
        return f"User: {self.user.username}, Task: {self.task.question_number}, Correct: {self.is_correct}"