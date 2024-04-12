from rest_framework import serializers
from .models import Post, CustomUser, Question, QuizCategory

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Make password write-only

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(password)  # Hash the password
        user.save()
        return user

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username']



class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'username', 'post']



class QuizSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    category_id = serializers.CharField(source='category.id', read_only=True)
    class Meta:
        model = Question
        fields = ['id', 'category', 'category_id', 'question', 'a', 'b', 'c', 'd', 'answer']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizCategory
        fields = ['id', 'name']
