from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Theory
from .serializers import TheorySerializer
from django.http import FileResponse
import os
from rest_framework.views import APIView

class TheoryListView(generics.ListAPIView):
    serializer_class = TheorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        level_id = self.kwargs['level_id']
        return Theory.objects.filter(level_id=level_id)

class TheoryDownloadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            theory = Theory.objects.get(pk=pk)
            file_path = theory.file.path
            if os.path.exists(file_path):
                return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=theory.file.name)
            else:
                return Response({'error': 'File not found'}, status=status.HTTP_404_NOT_FOUND)
        except Theory.DoesNotExist:
            return Response({'error': 'Theory not found'}, status=status.HTTP_404_NOT_FOUND)