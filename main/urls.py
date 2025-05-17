from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/tasks/', include('tasks.urls')),
    path('api/theory/', include('theory.urls')),
    path('api/user_tasks/', include('user_tasks.urls')),
]