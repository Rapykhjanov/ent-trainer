from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'profiles', views.ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('levels/', views.LevelListView.as_view(), name='level-list'),
    path('levels/<int:pk>/', views.LevelDetailView.as_view(), name='level-detail'),
]