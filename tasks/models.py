from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Task(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='tasks')
    difficulty = models.CharField(max_length=20)
    topic = models.CharField(max_length=100)
    question_number = models.IntegerField()
    question = models.TextField()
    # ИЗМЕНЕНИЕ ЗДЕСЬ: JSONField заменен на TextField
    answer_options = models.TextField(blank=True, null=True, help_text="Введите варианты ответа, разделяя их запятыми (например: 'Опция A, Опция B, Опция C').")
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.category.name} - {self.topic} - {self.question_number}"