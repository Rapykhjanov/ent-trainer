from rest_framework import serializers
from .models import Theory

class TheorySerializer(serializers.ModelSerializer):
    file = serializers.FileField(read_only=True)

    class Meta:
        model = Theory
        fields = '__all__'