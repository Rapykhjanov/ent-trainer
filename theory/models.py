from django.db import models

class Theory(models.Model):
    level = models.ForeignKey('users.Level', on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    file = models.FileField(upload_to='theory_files/')

    def __str__(self):
        return f"{self.level.name} - {self.topic}"