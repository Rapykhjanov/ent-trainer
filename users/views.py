from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from .models import User, Profile, Level
from .serializers import UserSerializer, ProfileSerializer, LevelSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

class LevelListView(generics.ListAPIView):
    queryset = Level.objects.all().order_by('order')
    serializer_class = LevelSerializer
    permission_classes = [permissions.IsAuthenticated]

class LevelDetailView(generics.RetrieveAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [permissions.IsAuthenticated]