from rest_framework import serializers
from .models import User, Profile, Level

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'phone_number', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Profile.objects.create(user=user)
        return user

class LevelSerializer(serializers.ModelSerializer):
     class Meta:
         model = Level
         fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    level = LevelSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ('id', 'user', 'level', 'points')
        read_only_fields = ('user',)