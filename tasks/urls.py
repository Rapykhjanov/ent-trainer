from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('categories/<int:category_id>/tasks/', views.TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('check-answer/', views.CheckAnswerView.as_view(), name='check-answer'),
    path('task-result/', views.TaskResultView.as_view(), name='task-result'),
]
