from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="ent_trainer_users_groups",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="ent_trainer_users_permissions",
        related_query_name="user",
    )

class Level(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    order = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, blank=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username