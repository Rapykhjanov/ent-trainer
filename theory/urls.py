from django.urls import path
from . import views

urlpatterns = [
    path('levels/<int:level_id>/theory/', views.TheoryListView.as_view(), name='theory-list'),
    path('theory/<int:pk>/download/', views.TheoryDownloadView.as_view(), name='theory-download'),
]